from keras.models import load_model
import pandas
import os.path, os


class BdController:
    def __init__(self):
        self.market = 'market.csv'
        self.trends = 'trends.csv'
        self.options = 'options.csv'

    def save(self, market, trends):
        if os.path.exists(self.market):
            os.remove(self.market)
        marketDF = pandas.DataFrame(market[1:], columns=market[0])
        marketDF.to_csv(self.market, index=False)

        if os.path.exists(self.trends):
            os.remove(self.trends)
        trendsDF = pandas.DataFrame(trends[1:], columns=trends[0])
        trendsDF.to_csv(self.trends, index=False)

    def data_exists(self):
        return os.path.exists(self.market) and os.path.exists(self.trends)

    def read_data(self):
        return pandas.read_csv(self.market), pandas.read_csv(self.trends)

    def read_options(self):
        return pandas.read_csv(self.options)

    def save_options(self, options, num):
        if os.path.exists(self.options):
            os.remove(self.options)
        optDF = pandas.DataFrame(columns=['Options', 'Trend', 'Model'])
        market = options[:num]
        trends = options[num:]
        i = 0
        for m in market:
            optDF.loc[i] = [m, False, False]
            i += 1
        for t in trends:
            optDF.loc[i] = [t, True, False]
            i += 1

        optDF.to_csv(self.options, index=False)

    def option_numeric_data(self, name):
        if os.path.exists(self.options):
            opt = pandas.read_csv(self.options)
            is_name = opt['Options']==name
            result = []
            if opt[is_name].iloc[0].Trend:
                data = pandas.read_csv(self.trends)
                is_name = data['SEARCH_STRING'] == name
                data = data[is_name].sort_values(by='DATETIME')
                data = list(data.TREND_SUM)
                result.append(data)
            else:
                data = pandas.read_csv(self.market)
                names = data['NAME'].unique()
                data = data.sort_values(by='TIMESTAMP')
                for n in names:
                    is_name = data['NAME'] == n
                    data_by_name = data[is_name]
                    data_by_name = data_by_name[name]
                    result.append(list(data_by_name))

            return result

    def updateOptionsModels(self, options):
        if os.path.exists(self.options):
            opt = pandas.read_csv(self.options)
            os.remove(self.options)
            for name in options:
                opt.loc[opt['Options']== name, ['Model']] = True
            opt.to_csv(self.options)


    def app_or_option(self, name):
        if os.path.exists(self.options):
            opt = pandas.read_csv(self.options)
            is_name = opt['Options'] == name
            return opt[is_name].iloc[0].Trend

    def save_model(self, model, name):
        if os.path.exists(name+'.h5'):
            os.remove(name+'.h5')
        model.save(name+'.h5')

    def read_model(self, name):
        if os.path.exists(name+'.h5'):
            return load_model(name+'.h5')


    def read_market(self):
        if os.path.exists(self.market):
            return pandas.read_csv(self.market)


