#!

import requests
import os
import json

grafana_port = 80
grafana_host = os.environ['GRAFANA_IP']
# grafana_host = '174.138.54.106'
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


# Remove all existing data sources
datasource_get = session.get(
    os.path.join(grafana_url, 'api', 'datasources'),
    headers={'content-type': 'application/json'})
print('Data Source get response: ' + str(datasource_get.status_code))
print(str(datasource_get.json()))

for datasource in datasource_get.json():
    datasource_delete = session.delete(
        os.path.join(grafana_url, 'api', 'datasources', str(datasource['id'])),
        headers={'content-type': 'application/json'})
    print('Datasource delete response: ' + str(datasource_delete.status_code))

# Add graphite datasource
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

# Delete the dashboard if it exists
dashboard_delete = session.delete(
    os.path.join(grafana_url, 'api', 'dashboards', 'db', 'recipe'),
    headers={'content-type': 'application/json'}
)
print('Recipe dashboard delete response:' + str(dashboard_delete.status_code))
print(str(dashboard_delete.json()))

# Add new dashboard
dashboard_post = session.post(
    os.path.join(grafana_url, 'api', 'dashboards', 'db'),
    data=json.dumps(
        {
        "dashboard": {
            "__inputs": [
                {
                    "name": "DS_DATASOURCE",
                    "label": "DataSource",
                    "description": "",
                    "type": "datasource",
                    "pluginId": "graphite",
                    "pluginName": "Graphite"
                }
            ],
            "__requires": [
                {
                    "type": "grafana",
                    "id": "grafana",
                    "name": "Grafana",
                    "version": "4.2.0"
                },
                {
                    "type": "panel",
                    "id": "graph",
                    "name": "Graph",
                    "version": ""
                },
                {
                    "type": "datasource",
                    "id": "graphite",
                    "name": "Graphite",
                    "version": "1.0.0"
                }
            ],
            "annotations": {
                "list": []
            },
            "editable": True,
            "gnetId": None,
            "graphTooltip": 0,
            "hideControls": False,
            "id": None,
            "links": [],
            "refresh": "30s",
            "rows": [
                {
                    "collapse": False,
                    "height": "250px",
                    "panels": [
                        {
                            "NonePointMode": "connected",
                            "aliasColors": {},
                            "bars": False,
                            "datasource": "${DS_DATASOURCE}",
                            "editable": True,
                            "error": False,
                            "fill": 1,
                            "grid": {},
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
                            "nullPointMode": "null",
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
                                    "refId": "A",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.getRecipes.mean, 'listRecipes')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "B",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.getRecipe.mean, 'getRecipe')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "C",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.postRecipe.mean, 'postRecipe')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "D",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.deleteRecipe.mean, 'deleteRecipe')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "E",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.putRecipe.mean, 'putRecipe')",
                                    "textEditor": False
                                }
                            ],
                            "thresholds": [],
                            "timeFrom": None,
                            "timeShift": None,
                            "title": "Recipe Mean Response Time",
                            "tooltip": {
                                "shared": True,
                                "sort": 0,
                                "value_type": "cumulative"
                            },
                            "type": "graph",
                            "xaxis": {
                                "mode": "time",
                                "name": None,
                                "show": True,
                                "values": []
                            },
                            "yaxes": [
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                },
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                }
                            ]
                        },
                        {
                            "NonePointMode": "connected",
                            "aliasColors": {},
                            "bars": False,
                            "datasource": "${DS_DATASOURCE}",
                            "editable": True,
                            "error": False,
                            "fill": 1,
                            "grid": {},
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
                            "nullPointMode": "null",
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
                                    "refId": "A",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.getRecipes.p999, 'listRecipes')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "B",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.getRecipe.p999, 'getRecipe')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "C",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.postRecipe.p999, 'postRecipe')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "D",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.deleteRecipe.p999, 'deleteRecipe')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "E",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.putRecipe.p999, 'putRecipe')",
                                    "textEditor": False
                                }
                            ],
                            "thresholds": [],
                            "timeFrom": None,
                            "timeShift": None,
                            "title": "Recipe P999",
                            "tooltip": {
                                "shared": True,
                                "sort": 0,
                                "value_type": "cumulative"
                            },
                            "type": "graph",
                            "xaxis": {
                                "mode": "time",
                                "name": None,
                                "show": True,
                                "values": []
                            },
                            "yaxes": [
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                },
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                }
                            ]
                        },
                        {
                            "NonePointMode": "connected",
                            "aliasColors": {},
                            "bars": False,
                            "datasource": "${DS_DATASOURCE}",
                            "editable": True,
                            "error": False,
                            "fill": 1,
                            "grid": {},
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
                            "nullPointMode": "null",
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
                                    "refId": "A",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.getRecipes.count, 'listRecipes')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "B",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.getRecipe.count, 'getRecipe')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "C",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.postRecipe.count, 'postRecipe')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "D",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.deleteRecipe.count, 'deleteRecipe')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "E",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeEndpoint.putRecipe.count, 'putRecipe')",
                                    "textEditor": False
                                }
                            ],
                            "thresholds": [],
                            "timeFrom": None,
                            "timeShift": None,
                            "title": "Recipe Hit Count",
                            "tooltip": {
                                "shared": True,
                                "sort": 0,
                                "value_type": "cumulative"
                            },
                            "type": "graph",
                            "xaxis": {
                                "mode": "time",
                                "name": None,
                                "show": True,
                                "values": []
                            },
                            "yaxes": [
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                },
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                }
                            ]
                        }
                    ],
                    "repeat": None,
                    "repeatIteration": None,
                    "repeatRowId": None,
                    "showTitle": False,
                    "title": "New row",
                    "titleSize": "h6"
                },
                {
                    "collapse": False,
                    "height": "250px",
                    "panels": [
                        {
                            "NonePointMode": "connected",
                            "aliasColors": {},
                            "bars": False,
                            "datasource": "${DS_DATASOURCE}",
                            "editable": True,
                            "error": False,
                            "fill": 1,
                            "grid": {},
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
                            "nullPointMode": "null",
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
                                    "refId": "A",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.getUser.mean, 'getUserById')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "B",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.getUserByEmail.mean, 'getUserByEmail')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "C",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.postUser.mean, 'postUser')",
                                    "textEditor": False
                                }
                            ],
                            "thresholds": [],
                            "timeFrom": None,
                            "timeShift": None,
                            "title": "User Mean Response Time",
                            "tooltip": {
                                "shared": True,
                                "sort": 0,
                                "value_type": "cumulative"
                            },
                            "type": "graph",
                            "xaxis": {
                                "mode": "time",
                                "name": None,
                                "show": True,
                                "values": []
                            },
                            "yaxes": [
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                },
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                }
                            ]
                        },
                        {
                            "NonePointMode": "connected",
                            "aliasColors": {},
                            "bars": False,
                            "datasource": "${DS_DATASOURCE}",
                            "editable": True,
                            "error": False,
                            "fill": 1,
                            "grid": {},
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
                            "nullPointMode": "null",
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
                                    "refId": "A",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.getUser.p999, 'getUserById')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "B",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.getUserByEmail.p999, 'getUserByEmail')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "C",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.postUser.p999, 'postUser')",
                                    "textEditor": False
                                }
                            ],
                            "thresholds": [],
                            "timeFrom": None,
                            "timeShift": None,
                            "title": "User P999",
                            "tooltip": {
                                "shared": True,
                                "sort": 0,
                                "value_type": "cumulative"
                            },
                            "type": "graph",
                            "xaxis": {
                                "mode": "time",
                                "name": None,
                                "show": True,
                                "values": []
                            },
                            "yaxes": [
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                },
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                }
                            ]
                        },
                        {
                            "NonePointMode": "connected",
                           
                            "aliasColors": {},
                            "bars": False,
                            "datasource": "${DS_DATASOURCE}",
                            "editable": True,
                            "error": False,
                            "fill": 1,
                            "grid": {},
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
                            "nullPointMode": "null",
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
                                    "refId": "A",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.getUser.count, 'getUserById')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "B",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.getUserByEmail.count, 'getUserByEmail')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "C",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.postUser.count, 'postUser')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "D",
                                    "target": "alias(scale(stats.gauges.recipe-service.com.poorknight.api.UserEndpoint.postUser.m1_rate, 100), 'New Users per Minute')",
                                    "textEditor": False
                                }
                            ],
                            "thresholds": [
                                {
                                    "colorMode": "critical",
                                    "fill": True,
                                    "line": True,
                                    "op": "gt",
                                    "value": 0
                                }
                            ],
                            "timeFrom": None,
                            "timeShift": None,
                            "title": "User Hit Count",
                            "tooltip": {
                                "shared": True,
                                "sort": 0,
                                "value_type": "cumulative"
                            },
                            "type": "graph",
                            "xaxis": {
                                "mode": "time",
                                "name": None,
                                "show": True,
                                "values": []
                            },
                            "yaxes": [
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                },
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                }
                            ]
                        }
                    ],
                    "repeat": None,
                    "repeatIteration": None,
                    "repeatRowId": None,
                    "showTitle": False,
                    "title": "New row",
                    "titleSize": "h6"
                },
                {
                    "collapse": False,
                    "height": "250px",
                    "panels": [
                        {
                            "NonePointMode": "connected",
                            "aliasColors": {},
                            "bars": False,
                            "datasource": "${DS_DATASOURCE}",
                            "editable": True,
                            "error": False,
                            "fill": 1,
                            "grid": {},
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
                            "nullPointMode": "null",
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
                                    "refId": "A",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.getRecipeBook.mean, 'getRecipeBook')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "B",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.postIdToRecipeBook.mean, 'postIdToRecipeBook')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "C",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.deleteRecipeFromBook.mean, 'deleteRecipeFromBook')",
                                    "textEditor": False
                                }
                            ],
                            "thresholds": [],
                            "timeFrom": None,
                            "timeShift": None,
                            "title": "RecipeBook Mean Response Time",
                            "tooltip": {
                                "shared": True,
                                "sort": 0,
                                "value_type": "cumulative"
                            },
                            "type": "graph",
                            "xaxis": {
                                "mode": "time",
                                "name": None,
                                "show": True,
                                "values": []
                            },
                            "yaxes": [
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                },
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                }
                            ]
                        },
                        {
                            "NonePointMode": "connected",
                            "aliasColors": {},
                            "bars": False,
                            "datasource": "${DS_DATASOURCE}",
                            "editable": True,
                            "error": False,
                            "fill": 1,
                            "grid": {},
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
                            "nullPointMode": "null",
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
                                    "refId": "A",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.getRecipeBook.p999, 'getRecipeBook')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "B",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.postIdToRecipeBook.p999, 'postIdToRecipeBook')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "C",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.deleteRecipeFromBook.p999, 'deleteRecipeFromBook')",
                                    "textEditor": False
                                }
                            ],
                            "thresholds": [],
                            "timeFrom": None,
                            "timeShift": None,
                            "title": "RecipeBook P999",
                            "tooltip": {
                                "shared": True,
                                "sort": 0,
                                "value_type": "cumulative"
                            },
                            "type": "graph",
                            "xaxis": {
                                "mode": "time",
                                "name": None,
                                "show": True,
                                "values": []
                            },
                            "yaxes": [
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                },
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                }
                            ]
                        },
                        {
                            "NonePointMode": "connected",
                            "aliasColors": {},
                            "bars": False,
                            "datasource": "${DS_DATASOURCE}",
                            "editable": True,
                            "error": False,
                            "fill": 1,
                            "grid": {},
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
                            "nullPointMode": "null",
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
                                    "refId": "A",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.getRecipeBook.count, 'getRecipeBook')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "B",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.postIdToRecipeBook.count, 'postIdToRecipeBook')",
                                    "textEditor": False
                                },
                                {
                                    "refId": "C",
                                    "target": "alias(stats.gauges.recipe-service.com.poorknight.api.RecipeBookEndpoint.deleteRecipeFromBook.count, 'deleteRecipeFromBook')",
                                    "textEditor": False
                                }
                            ],
                            "thresholds": [],
                            "timeFrom": None,
                            "timeShift": None,
                            "title": "RecipeBook Count",
                            "tooltip": {
                                "shared": True,
                                "sort": 0,
                                "value_type": "cumulative"
                            },
                            "type": "graph",
                            "xaxis": {
                                "mode": "time",
                                "name": None,
                                "show": True,
                                "values": []
                            },
                            "yaxes": [
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                },
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                }
                            ]
                        }
                    ],
                    "repeat": None,
                    "repeatIteration": None,
                    "repeatRowId": None,
                    "showTitle": False,
                    "title": "New row",
                    "titleSize": "h6"
                },
                {
                    "collapse": False,
                    "height": "250px",
                    "panels": [
                        {
                            "NonePointMode": "connected",
                            "aliasColors": {},
                            "bars": False,
                            "datasource": "${DS_DATASOURCE}",
                            "editable": True,
                            "error": False,
                            "fill": 1,
                            "grid": {},
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
                            "nullPointMode": "null",
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
                                    "refId": "A",
                                    "target": "stats.counters.statsd.bad_lines_seen.count"
                                },
                                {
                                    "refId": "B",
                                    "target": "stats.counters.statsd.packets_received.rate"
                                }
                            ],
                            "thresholds": [],
                            "timeFrom": None,
                            "timeShift": None,
                            "title": "StatsD Received Data",
                            "tooltip": {
                                "shared": True,
                                "sort": 0,
                                "value_type": "cumulative"
                            },
                            "type": "graph",
                            "xaxis": {
                                "mode": "time",
                                "name": None,
                                "show": True,
                                "values": []
                            },
                            "yaxes": [
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                },
                                {
                                    "format": "short",
                                    "logBase": 1,
                                    "max": None,
                                    "min": None,
                                    "show": True
                                }
                            ]
                        }
                    ],
                    "repeat": None,
                    "repeatIteration": None,
                    "repeatRowId": None,
                    "showTitle": False,
                    "title": "Row",
                    "titleSize": "h6"
                }
            ],
            "schemaVersion": 14,
            "style": "dark",
            "tags": [],
            "templating": {
                "list": []
            },
            "time": {
                "from": "now-24h",
                "to": "now"
            },
            "timepicker": {
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
            },
            "timezone": "browser",
            "title": "Recipe",
            "version": 4
        }
    }
    ),
    headers={'content-type': 'application/json'}
)

print('Dashboard creation response: ' + str(dashboard_post.status_code))
print(str(dashboard_post.json()))