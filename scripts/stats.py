#!/usr/bin/env python

import os
import sys
import yaml
import numpy as np
import matplotlib.pyplot as plt

def gather(filename):
    KEYS = ('2k_cpu_p3m',
            '20k_cpu_p3m',
            '200k_cpu_p3m',
            '2k_gpu_p3m',
            '20k_gpu_p3m',
            '200k_gpu_p3m',
            '2m_gpu_p3m',
            '20m_gpu_p3m',
            '200m_gpu_p3m',
            '2k_cudampi',
            '20k_cudampi',
            '200k_cudampi',
            '2m_cudampi',
            '20m_cudampi',
            '200m_cudampi',
            'vsum_cpu',
            'vsum_gpu',
            'vsum_cudampi',
            'vsum_mpi',)
    def read():
        assert os.path.exists(filename)
        def next_record():
            with open(filename, 'r') as f:
                for rec in f:
                    yield rec.strip('()\n')
        def parse_record(rec):
            (k, u, s, r, p,) = rec.split(' ')
            return (k, float(u), float(s), float(r), int(p),)
        return list(parse_record(x) for x in next_record())
    def compute(records, key):
        rows = list(x for x in records if key in x[0])
        if len(rows) == 0:
            return {}
        user = list(x[1] for x in rows)
        system = list(x[2] for x in rows)
        real = list(x[3] for x in rows)
        cpu = list(x[4] for x in rows)
        return {'User':   (np.average(user),
                           np.mean(user),
                           np.median(user),
                           np.std(user),
                           np.var(user),),
                'System': (np.average(system),
                           np.mean(system),
                           np.median(system),
                           np.std(system),
                           np.var(system),),
                'Real':   (np.average(real),
                           np.mean(real),
                           np.median(real),
                           np.std(real),
                           np.var(real),),
                'CPU%':   (np.average(cpu),
                           np.mean(cpu),
                           np.median(cpu),
                           np.std(cpu),
                           np.var(cpu),),}
    uncomputed_recs = read()
    computed_recs = {}
    for k in KEYS:
        computed_recs[k] = compute(uncomputed_recs, k)
    return computed_recs

def printout_stats(stats):
    for k, v in stats.items():
        print('Data Set: %s' % k)
        if len(v) == 0:
            print('No Data!')
            continue
        for t, d in v.items():
            print("    %s:" % t)
            print("""
        Average:   %f
        Mean:      %f
        Median:    %f
        Std:       %f
        Var:       %f""" % d)

def bar_chart(title, x, y, err, filename=None, xlabel=None, ylabel=None):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    width = 0.35
    ind = np.arange(len(y))
    ax.bar(ind + width / 2, y, width, facecolor='#777777', yerr=err)
    ax.set_xticks(ind + width)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticklabels(x)
    plt.savefig(filename, dpi=800, format='svg')

def select(db, x, key, i):
    return list(db[k][key][i] for k in x)

def generate_charts(results_fname, barcharts_fname):
    db = gather(results_fname)
    def loadyaml(fname):
        with open(fname, 'r') as f:
            return yaml.load(f)
    def create_bar(chart):
        x = chart['keys']
        y = select(db, x, chart['data'], 0)
        err = list(0 for i in range(len(y)))
        if chart['std']:
            err = select(db, x, chart['data'], 3)
        bar_chart(chart['title'], x, y, err,
                  filename=chart.get('filename'),
                  xlabel=chart.get('xlabel', ''),
                  ylabel=chart.get('ylabel', ''))
    charts = loadyaml(barcharts_fname)
    for k,c in charts.items():
        if c['type'] == 'bar':
            create_bar(c)

if __name__ == '__main__':
    if len(sys.argv[1:]) >= 2:
        generate_charts(sys.argv[1], sys.argv[2])
