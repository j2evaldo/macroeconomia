import pandas as pd

class EconometriaUtils:

    def trimestraliza_expectativa(self, exp_ipca):
        exp_ipca_aux = (
          exp_ipca
         .assign(Year = lambda x: pd.to_datetime(x.Data).dt.year,
                 Month = lambda x: pd.to_datetime(x.Data).dt.month)
          .groupby(by = ['Year', 'Month'])
          .agg({'Mediana' : 'mean'})
          .reset_index()
          .assign(Quarter = lambda x: pd.to_datetime(x[['Year', 'Month']].assign(Day = 1)),
                  date_quarter = lambda x: pd.PeriodIndex(x['Quarter'], freq = 'Q'))
          .groupby(by = 'date_quarter')
          .agg(ipca_exp_12m = ('Mediana', 'mean'))
          .reset_index()
        )
        return exp_ipca_aux