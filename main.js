SlidesView = Backbone.View.extend({
    initialize: function () {
        jQuery.ajax({
            url: "https://raw.github.com/mpitx/mpitx.github.com/master/slides.html",
            success: function (htmlContent) {
                this.templateContent = htmlContent;
            }
        });
        this.render();
    },
    render: function () {
        jQuery(this.el).html(this.templateContent);
    },
});

ReportView = Backbone.View.extend({
    templateContent: "<h4>Report</h4>",
    initialize: function () {
        jQuery.ajax({
            url: "https://raw.github.com/mpitx/mpitx.github.com/master/report.html",
            success: function (htmlContent) {
                this.templateContent = htmlContent;
            }
        });
        this.render();
    },
    render: function () {
        jQuery(this.el).html(this.templateContent);
    },
});

CodeView = Backbone.View.extend({
    templateContent: "<h4>Projects and Code</h4>",
    initialize: function () {
        jQuery.ajax({
            url: "https://raw.github.com/mpitx/mpitx.github.com/master/code.html",
            success: function (htmlContent) {
                this.templateContent = htmlContent;
            }
        });
        this.render();
    },
    render: function () {
        jQuery(this.el).html(this.templateContent);
    },
});

SideBarView = Backbone.View.extend({
    templateContent: "<ul><li><a id=\"slidesLink\">Slides</a></li>"
                   + "<li><a id=\"reportLink\">Report</a></li>"
                   + "<li><a id=\"codeLink\">Code and Projects</a></li>",
    initialize: function () {
        this.render();
    },
    render: function () {
        jQuery(this.el).html(this.templateContent);
    },
    events: {
        "click #slidesLink": "viewSlidesView",
        "click #reportLink": "viewReportView",
        "click #codeLink": "viewCodeView"
    },
    viewSlidesView: function () {
        (new SlidesView( { el: jQuery("#MainContent") } ));
    },
    viewReportView: function () {
        (new ReportView( { el: jQuery("#MainContent") } ));
    },
    viewCodeView: function () {
        (new CodeView( { el: jQuery("#MainContent") } ));
    }
});

$(function () {
    var sideBar = new SideBarView( { el: jQuery("#SideBar") } );
});
