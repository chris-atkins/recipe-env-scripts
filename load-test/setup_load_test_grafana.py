#!

import requests
import os
import json

grafana_port = 80
grafana_host = os.environ['GRAFANA_IP']
# grafana_host = '45.55.153.110'
print('Grafana Host: ' + grafana_host)

grafana_url = os.path.join('http://', '%s:%u' % (grafana_host, grafana_port))
session = requests.Session()
login_post = session.post(
    os.path.join(grafana_url, 'login'),
    data=json.dumps({
        'user': 'admin',
        'email': '',
        'password': 'admin' }),
    headers={'content-type': 'application/json'})

print('Login response: ' + str(login_post.status_code))
print(str(login_post.json()))


# Add new datasource
datasources_post = session.post(
    os.path.join(grafana_url, 'api', 'datasources'),
    data=json.dumps({
        "name":"DataSource",
        "type":"graphite",
        "url":"http://localhost:8000",
        "access":"proxy",
        "jsonData":{}}),
    headers={'content-type': 'application/json'})

print('Data Source creation response: ' + str(datasources_post.status_code))
print(str(datasources_post.json()))


# Add new dashboard
dashboard_post = session.post(
    os.path.join(grafana_url, 'api', 'dashboards', 'db'),
    data=json.dumps({
        "overwrite": False,
        "dashboard": {
        "id": None,
        "title": "Recipe",
        "originalTitle": "Recipe",
        "tags": [],
        "style": "dark",
        "timezone": "browser",
        "editable": True,
        "hideControls": False,
        "sharedCrosshair": False,
        "rows": [
            {
                "collapse": False,
                "editable": True,
                "height": "250px",
                "panels": [
                    {
                        "aliasColors": {},
                        "bars": False,
                        "datasource": "DataSource",
                        "editable": True,
                        "error": False,
                        "fill": 1,
                        "grid": {
                            "leftLogBase": 1,
                            "leftMax": None,
                            "leftMin": None,
                            "rightLogBase": 1,
                            "rightMax": None,
                            "rightMin": None,
                            "threshold1": None,
                            "threshold1Color": "rgba(216, 200, 27, 0.27)",
                            "threshold2": None,
                            "threshold2Color": "rgba(234, 112, 112, 0.22)"
                        },
                        "id": 2,
                        "legend": {
                            "avg": False,
                            "current": False,
                            "max": False,
                            "min": False,
                            "show": True,
                            "total": False,
                            "values": False
                        },
                        "lines": True,
                        "linewidth": 2,
                        "links": [],
                        "NonePointMode": "connected",
                        "percentage": False,
                        "pointradius": 5,
                        "points": False,
                        "renderer": "flot",
                        "seriesOverrides": [],
                        "span": 4,
                        "stack": False,
                        "steppedLine": False,
                        "targets": [
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.getRecipes.mean, 'listRecipes')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.getRecipe.mean, 'getRecipe')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.postRecipe.mean, 'postRecipe')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.deleteRecipe.mean, 'deleteRecipe')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.putRecipe.mean, 'putRecipe')",
                                "textEditor": False
                            }
                        ],
                        "timeFrom": None,
                        "timeShift": None,
                        "title": "Recipe Mean Response Time",
                        "tooltip": {
                            "shared": True,
                            "value_type": "cumulative"
                        },
                        "type": "graph",
                        "x-axis": True,
                        "y-axis": True,
                        "y_formats": [
                            "short",
                            "short"
                        ]
                    },
                    {
                        "aliasColors": {},
                        "bars": False,
                        "datasource": "DataSource",
                        "editable": True,
                        "error": False,
                        "fill": 1,
                        "grid": {
                            "leftLogBase": 1,
                            "leftMax": None,
                            "leftMin": None,
                            "rightLogBase": 1,
                            "rightMax": None,
                            "rightMin": None,
                            "threshold1": None,
                            "threshold1Color": "rgba(216, 200, 27, 0.27)",
                            "threshold2": None,
                            "threshold2Color": "rgba(234, 112, 112, 0.22)"
                        },
                        "id": 4,
                        "legend": {
                            "avg": False,
                            "current": False,
                            "max": False,
                            "min": False,
                            "show": True,
                            "total": False,
                            "values": False
                        },
                        "lines": True,
                        "linewidth": 2,
                        "links": [],
                        "NonePointMode": "connected",
                        "percentage": False,
                        "pointradius": 5,
                        "points": False,
                        "renderer": "flot",
                        "seriesOverrides": [],
                        "span": 4,
                        "stack": False,
                        "steppedLine": False,
                        "targets": [
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.getRecipes.p999, 'listRecipes')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.getRecipe.p999, 'getRecipe')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.postRecipe.p999, 'postRecipe')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.deleteRecipe.p999, 'deleteRecipe')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.putRecipe.p999, 'putRecipe')",
                                "textEditor": False
                            }
                        ],
                        "timeFrom": None,
                        "timeShift": None,
                        "title": "Recipe P999",
                        "tooltip": {
                            "shared": True,
                            "value_type": "cumulative"
                        },
                        "type": "graph",
                        "x-axis": True,
                        "y-axis": True,
                        "y_formats": [
                            "short",
                            "short"
                        ]
                    },
                    {
                        "aliasColors": {},
                        "bars": False,
                        "datasource": "DataSource",
                        "editable": True,
                        "error": False,
                        "fill": 1,
                        "grid": {
                            "leftLogBase": 1,
                            "leftMax": None,
                            "leftMin": None,
                            "rightLogBase": 1,
                            "rightMax": None,
                            "rightMin": None,
                            "threshold1": None,
                            "threshold1Color": "rgba(216, 200, 27, 0.27)",
                            "threshold2": None,
                            "threshold2Color": "rgba(234, 112, 112, 0.22)"
                        },
                        "id": 5,
                        "legend": {
                            "avg": False,
                            "current": False,
                            "max": False,
                            "min": False,
                            "show": True,
                            "total": False,
                            "values": False
                        },
                        "lines": True,
                        "linewidth": 2,
                        "links": [],
                        "NonePointMode": "connected",
                        "percentage": False,
                        "pointradius": 5,
                        "points": False,
                        "renderer": "flot",
                        "seriesOverrides": [],
                        "span": 4,
                        "stack": False,
                        "steppedLine": False,
                        "targets": [
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.getRecipes.count, 'listRecipes')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.getRecipe.count, 'getRecipe')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.postRecipe.count, 'postRecipe')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.deleteRecipe.count, 'deleteRecipe')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.putRecipe.count, 'putRecipe')",
                                "textEditor": False
                            }
                        ],
                        "timeFrom": None,
                        "timeShift": None,
                        "title": "Recipe Hit Count",
                        "tooltip": {
                            "shared": True,
                            "value_type": "cumulative"
                        },
                        "type": "graph",
                        "x-axis": True,
                        "y-axis": True,
                        "y_formats": [
                            "short",
                            "short"
                        ]
                    }
                ],
                "title": "New row"
            },
            {
                "collapse": False,
                "editable": True,
                "height": "250px",
                "panels": [
                    {
                        "aliasColors": {},
                        "bars": False,
                        "datasource": "DataSource",
                        "editable": True,
                        "error": False,
                        "fill": 1,
                        "grid": {
                            "leftLogBase": 1,
                            "leftMax": None,
                            "leftMin": None,
                            "rightLogBase": 1,
                            "rightMax": None,
                            "rightMin": None,
                            "threshold1": None,
                            "threshold1Color": "rgba(216, 200, 27, 0.27)",
                            "threshold2": None,
                            "threshold2Color": "rgba(234, 112, 112, 0.22)"
                        },
                        "id": 3,
                        "legend": {
                            "avg": False,
                            "current": False,
                            "max": False,
                            "min": False,
                            "show": True,
                            "total": False,
                            "values": False
                        },
                        "lines": True,
                        "linewidth": 2,
                        "links": [],
                        "NonePointMode": "connected",
                        "percentage": False,
                        "pointradius": 5,
                        "points": False,
                        "renderer": "flot",
                        "seriesOverrides": [],
                        "span": 4,
                        "stack": False,
                        "steppedLine": False,
                        "targets": [
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.getUser.mean, 'getUserById')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.getUserByEmail.mean, 'getUserByEmail')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.postUser.mean, 'postUser')",
                                "textEditor": False
                            }
                        ],
                        "timeFrom": None,
                        "timeShift": None,
                        "title": "User Mean Response Time",
                        "tooltip": {
                            "shared": True,
                            "value_type": "cumulative"
                        },
                        "type": "graph",
                        "x-axis": True,
                        "y-axis": True,
                        "y_formats": [
                            "short",
                            "short"
                        ]
                    },
                    {
                        "aliasColors": {},
                        "bars": False,
                        "datasource": "DataSource",
                        "editable": True,
                        "error": False,
                        "fill": 1,
                        "grid": {
                            "leftLogBase": 1,
                            "leftMax": None,
                            "leftMin": None,
                            "rightLogBase": 1,
                            "rightMax": None,
                            "rightMin": None,
                            "threshold1": None,
                            "threshold1Color": "rgba(216, 200, 27, 0.27)",
                            "threshold2": None,
                            "threshold2Color": "rgba(234, 112, 112, 0.22)"
                        },
                        "id": 6,
                        "legend": {
                            "avg": False,
                            "current": False,
                            "max": False,
                            "min": False,
                            "show": True,
                            "total": False,
                            "values": False
                        },
                        "lines": True,
                        "linewidth": 2,
                        "links": [],
                        "NonePointMode": "connected",
                        "percentage": False,
                        "pointradius": 5,
                        "points": False,
                        "renderer": "flot",
                        "seriesOverrides": [],
                        "span": 4,
                        "stack": False,
                        "steppedLine": False,
                        "targets": [
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.getUser.p999, 'getUserById')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.getUserByEmail.p999, 'getUserByEmail')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.postUser.p999, 'postUser')",
                                "textEditor": False
                            }
                        ],
                        "timeFrom": None,
                        "timeShift": None,
                        "title": "User P999",
                        "tooltip": {
                            "shared": True,
                            "value_type": "cumulative"
                        },
                        "type": "graph",
                        "x-axis": True,
                        "y-axis": True,
                        "y_formats": [
                            "short",
                            "short"
                        ]
                    },
                    {
                        "aliasColors": {},
                        "bars": False,
                        "datasource": "DataSource",
                        "editable": True,
                        "error": False,
                        "fill": 1,
                        "grid": {
                            "leftLogBase": 1,
                            "leftMax": None,
                            "leftMin": None,
                            "rightLogBase": 1,
                            "rightMax": None,
                            "rightMin": None,
                            "threshold1": None,
                            "threshold1Color": "rgba(216, 200, 27, 0.27)",
                            "threshold2": None,
                            "threshold2Color": "rgba(234, 112, 112, 0.22)"
                        },
                        "id": 7,
                        "legend": {
                            "avg": False,
                            "current": False,
                            "max": False,
                            "min": False,
                            "show": True,
                            "total": False,
                            "values": False
                        },
                        "lines": True,
                        "linewidth": 2,
                        "links": [],
                        "NonePointMode": "connected",
                        "percentage": False,
                        "pointradius": 5,
                        "points": False,
                        "renderer": "flot",
                        "seriesOverrides": [],
                        "span": 4,
                        "stack": False,
                        "steppedLine": False,
                        "targets": [
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.getUser.count, 'getUserById')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.getUserByEmail.count, 'getUserByEmail')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.postUser.count, 'postUser')",
                                "textEditor": False
                            }
                        ],
                        "timeFrom": None,
                        "timeShift": None,
                        "title": "User Hit Count",
                        "tooltip": {
                            "shared": True,
                            "value_type": "cumulative"
                        },
                        "type": "graph",
                        "x-axis": True,
                        "y-axis": True,
                        "y_formats": [
                            "short",
                            "short"
                        ]
                    }
                ],
                "title": "New row"
            },
            {
                "collapse": False,
                "editable": True,
                "height": "250px",
                "panels": [
                    {
                        "aliasColors": {},
                        "bars": False,
                        "datasource": "DataSource",
                        "editable": True,
                        "error": False,
                        "fill": 1,
                        "grid": {
                            "leftLogBase": 1,
                            "leftMax": None,
                            "leftMin": None,
                            "rightLogBase": 1,
                            "rightMax": None,
                            "rightMin": None,
                            "threshold1": None,
                            "threshold1Color": "rgba(216, 200, 27, 0.27)",
                            "threshold2": None,
                            "threshold2Color": "rgba(234, 112, 112, 0.22)"
                        },
                        "id": 8,
                        "legend": {
                            "avg": False,
                            "current": False,
                            "max": False,
                            "min": False,
                            "show": True,
                            "total": False,
                            "values": False
                        },
                        "lines": True,
                        "linewidth": 2,
                        "links": [],
                        "NonePointMode": "connected",
                        "percentage": False,
                        "pointradius": 5,
                        "points": False,
                        "renderer": "flot",
                        "seriesOverrides": [],
                        "span": 4,
                        "stack": False,
                        "steppedLine": False,
                        "targets": [
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.getRecipeBook.mean, 'getRecipeBook')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.postIdToRecipeBook.mean, 'postIdToRecipeBook')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.deleteRecipeFromBook.mean, 'deleteRecipeFromBook')",
                                "textEditor": False
                            }
                        ],
                        "timeFrom": None,
                        "timeShift": None,
                        "title": "RecipeBook Mean Response Time",
                        "tooltip": {
                            "shared": True,
                            "value_type": "cumulative"
                        },
                        "type": "graph",
                        "x-axis": True,
                        "y-axis": True,
                        "y_formats": [
                            "short",
                            "short"
                        ]
                    },
                    {
                        "aliasColors": {},
                        "bars": False,
                        "datasource": "DataSource",
                        "editable": True,
                        "error": False,
                        "fill": 1,
                        "grid": {
                            "leftLogBase": 1,
                            "leftMax": None,
                            "leftMin": None,
                            "rightLogBase": 1,
                            "rightMax": None,
                            "rightMin": None,
                            "threshold1": None,
                            "threshold1Color": "rgba(216, 200, 27, 0.27)",
                            "threshold2": None,
                            "threshold2Color": "rgba(234, 112, 112, 0.22)"
                        },
                        "id": 9,
                        "legend": {
                            "avg": False,
                            "current": False,
                            "max": False,
                            "min": False,
                            "show": True,
                            "total": False,
                            "values": False
                        },
                        "lines": True,
                        "linewidth": 2,
                        "links": [],
                        "NonePointMode": "connected",
                        "percentage": False,
                        "pointradius": 5,
                        "points": False,
                        "renderer": "flot",
                        "seriesOverrides": [],
                        "span": 4,
                        "stack": False,
                        "steppedLine": False,
                        "targets": [
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.getRecipeBook.p999, 'getRecipeBook')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.postIdToRecipeBook.p999, 'postIdToRecipeBook')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.deleteRecipeFromBook.p999, 'deleteRecipeFromBook')",
                                "textEditor": False
                            }
                        ],
                        "timeFrom": None,
                        "timeShift": None,
                        "title": "RecipeBook P999",
                        "tooltip": {
                            "shared": True,
                            "value_type": "cumulative"
                        },
                        "type": "graph",
                        "x-axis": True,
                        "y-axis": True,
                        "y_formats": [
                            "short",
                            "short"
                        ]
                    },
                    {
                        "aliasColors": {},
                        "bars": False,
                        "datasource": "DataSource",
                        "editable": True,
                        "error": False,
                        "fill": 1,
                        "grid": {
                            "leftLogBase": 1,
                            "leftMax": None,
                            "leftMin": None,
                            "rightLogBase": 1,
                            "rightMax": None,
                            "rightMin": None,
                            "threshold1": None,
                            "threshold1Color": "rgba(216, 200, 27, 0.27)",
                            "threshold2": None,
                            "threshold2Color": "rgba(234, 112, 112, 0.22)"
                        },
                        "id": 10,
                        "legend": {
                            "avg": False,
                            "current": False,
                            "max": False,
                            "min": False,
                            "show": True,
                            "total": False,
                            "values": False
                        },
                        "lines": True,
                        "linewidth": 2,
                        "links": [],
                        "NonePointMode": "connected",
                        "percentage": False,
                        "pointradius": 5,
                        "points": False,
                        "renderer": "flot",
                        "seriesOverrides": [],
                        "span": 4,
                        "stack": False,
                        "steppedLine": False,
                        "targets": [
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.getRecipeBook.count, 'getRecipeBook')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.postIdToRecipeBook.count, 'postIdToRecipeBook')",
                                "textEditor": False
                            },
                            {
                                "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.deleteRecipeFromBook.count, 'deleteRecipeFromBook')",
                                "textEditor": False
                            }
                        ],
                        "timeFrom": None,
                        "timeShift": None,
                        "title": "RecipeBook Count",
                        "tooltip": {
                            "shared": True,
                            "value_type": "cumulative"
                        },
                        "type": "graph",
                        "x-axis": True,
                        "y-axis": True,
                        "y_formats": [
                            "short",
                            "short"
                        ]
                    }
                ],
                "title": "New row"
            },
            {
                "collapse": False,
                "editable": True,
                "height": "250px",
                "panels": [
                    {
                        "aliasColors": {},
                        "bars": False,
                        "datasource": "DataSource",
                        "editable": True,
                        "error": False,
                        "fill": 1,
                        "grid": {
                            "leftLogBase": 1,
                            "leftMax": None,
                            "leftMin": None,
                            "rightLogBase": 1,
                            "rightMax": None,
                            "rightMin": None,
                            "threshold1": None,
                            "threshold1Color": "rgba(216, 200, 27, 0.27)",
                            "threshold2": None,
                            "threshold2Color": "rgba(234, 112, 112, 0.22)"
                        },
                        "id": 1,
                        "legend": {
                            "avg": False,
                            "current": False,
                            "max": False,
                            "min": False,
                            "show": True,
                            "total": False,
                            "values": False
                        },
                        "lines": True,
                        "linewidth": 2,
                        "links": [],
                        "NonePointMode": "connected",
                        "percentage": False,
                        "pointradius": 5,
                        "points": False,
                        "renderer": "flot",
                        "seriesOverrides": [],
                        "span": 12,
                        "stack": False,
                        "steppedLine": False,
                        "targets": [
                            {
                                "target": "stats.counters.statsd.bad_lines_seen.count"
                            },
                            {
                                "target": "stats.counters.statsd.packets_received.rate"
                            }
                        ],
                        "timeFrom": None,
                        "timeShift": None,
                        "title": "StatsD Received Data",
                        "tooltip": {
                            "shared": True,
                            "value_type": "cumulative"
                        },
                        "type": "graph",
                        "x-axis": True,
                        "y-axis": True,
                        "y_formats": [
                            "short",
                            "short"
                        ]
                    }
                ],
                "title": "Row"
            }
        ],
        "nav": [
            {
                "collapse": False,
                "enable": True,
                "notice": False,
                "now": True,
                "refresh_intervals": [
                    "5s",
                    "10s",
                    "30s",
                    "1m",
                    "5m",
                    "15m",
                    "30m",
                    "1h",
                    "2h",
                    "1d"
                ],
                "status": "Stable",
                "time_options": [
                    "5m",
                    "15m",
                    "1h",
                    "6h",
                    "12h",
                    "24h",
                    "2d",
                    "7d",
                    "30d"
                ],
                "type": "timepicker"
            }
        ],
        "time": {
            "from": "now-1h",
            "to": "now"
        },
        "templating": {
            "list": []
        },
        "annotations": {
            "list": []
        },
        "schemaVersion": 6,
        "version": 38,
        "links": []
    }}),
    headers={'content-type': 'application/json'}
)

print('Dashboard creation response: ' + str(dashboard_post.status_code))
print(str(dashboard_post.json()))