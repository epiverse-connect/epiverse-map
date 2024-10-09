# API design

## Requirements

* API should be relatively easy to call (i.e., through a single GET/POST request)
* It should be reasonably responsive by default (<5s)
* API returns JSON object
* If the schema is expected to change a lot, versioned API routes would be preferable.

## Querying the API

The API call includes all the results to be included in the map. This helps facilitate scheduled updates and reduces the need for repeat querying. An example query URL would be `api.epiverse.org/map` (versioned could look like `api.epiverse.org/v1/map`).

## Response

The response for the API is one JSON object containing an array of package names, the relevant metadata, and their respective embedding scores.

```json
{
  "results": 2,
  "data": [
    {
      "package": "epidemics",
      "logo": "https://epiverse-trace.github.io/epidemics/logo.svg",
      "website": "https://epiverse-trace.github.io/epidemics",
      "source": "https://github.com/epiverse-trace/epidemics",
      "vignettes": [
          "https://epiverse-trace.github.io/epidemics/articles/modelling_interventions.html",
          "https://epiverse-trace.github.io/epidemics/articles/modelling_multiple_interventions.html"
      ],
      "coord1": 0.384,
      "coord2": 0.684,
    },
    ...
  ]
}
```
