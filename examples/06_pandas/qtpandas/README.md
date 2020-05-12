# QtPandas

Widget support for the [pandas](http://pandas.pydata.org/) Python module.

## Goal

Be included as an additional sub-module for [PySide2](https://pyside.org).

## Details

Include visual representation for
[DataFrame](http://pandas.pydata.org/pandas-docs/stable/reference/frame.html)
and for [Series](http://pandas.pydata.org/pandas-docs/stable/reference/series.html).

* Widget based in `QTableView`.
* Widged-based tool to manipulate *DataFrame* and *Series*.
  * Add/remove columns/rows.
  * Apply filters to columns/rows.
  * Join/split DataFrames.
* Plots based in `QtCharts` or [matplotlib](https://matplotlib.org/).
