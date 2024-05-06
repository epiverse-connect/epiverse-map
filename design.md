# Epiverse visual map

## User persona & user story

This work is mostly targeted at the following persona:

- Pandemic & Epidemic Intelligence tool implementer
- Pandemic & Epidemic Intelligence tool creator
- Domain expert

with the following user story:

> I want to quickly & visually understand what Epiverse is about, and its niche in the ecosystem of data science tools for Epidemiology

## Design options and user feedback

3 options have been identified to address the user stories:

+--------------+--------------------------------------------------------+-----------------------------------------------------+----------------------------------------------------------------------------------+
| Solution     | Benefits                                               | Limitations                                         | Examples                                                                         |
+==============+========================================================+=====================================================+==================================================================================+
| cards        | -   More details on specific packages                  | -   Does not explicit links between packages        | -   [r-universe](https://epiverse-trace.r-universe.dev)                          |
|              |                                                        |                                                     |                                                                                  |
|              |                                                        |                                                     | -   [rOpenSci](https://ropensci.org/packages/image-processing/)                  |
+--------------+--------------------------------------------------------+-----------------------------------------------------+----------------------------------------------------------------------------------+
| network      | -   Explicit interactions & relations between packages | -   Does not much give info on individual packages  | -   [Original Epiverse-Connect](https://github.com/epiverse-connect/NetworkViz)  |
|              |                                                        |                                                     |                                                                                  |
|              |                                                        | -   May be difficult to automate link definition    |                                                                                  |
+--------------+--------------------------------------------------------+-----------------------------------------------------+----------------------------------------------------------------------------------+
| map          | -   Can be fully automated                             | -   Does not explicit interactions between packages | -   [Map of GitHub](https://anvaka.github.io/map-of-github/)                     |
|              |                                                        |                                                     |                                                                                  |
|              | -   Clarify package scope                              |                                                     |                                                                                  |
+--------------+--------------------------------------------------------+-----------------------------------------------------+----------------------------------------------------------------------------------+

These three options, with their pros and cons have been presented to a panel of potential users and they recommended moving forward with a hybrid of the network and cards options.

The network is a good way to get a quick high-level overview of the ecosystem, and Epiverse position in the ecosystem. The cards allow us to see the details of each package.

## Requirements

The tool should:

- represent R packages from [the CRAN Task View in Epidemiology](https://github.com/cran-task-views/Epidemiology) as nodes of the network
- highlight Epiverse packages in a different color
- allow clicking on a node to see the details of the package

## Previous and related work

- https://github.com/epiverse-connect/NetworkViz, creating a network of packages, and external data sources, based on manual input of interoperability level
- https://github.com/epiverse-connect/dashboard, creating a network of packages from the Task View based on their dependency relationships
