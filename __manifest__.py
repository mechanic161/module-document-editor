{
    "name": "Document Editor",
    "version": "18.0.1.0.1",
    "author": "Mechanic",
    "description": "Custom module for viewing and editing documents",
    "license": "LGPL-3",
    "depends": [
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",

        "views/module_geo_views_actions.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "module_geo/static/lib/html2canvas/html2canvas.min.js",

            "module_geo/static/src/js/geo_search_helper.js",
        ],
    },
}
