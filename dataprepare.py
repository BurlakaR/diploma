import numpy
import pandas


class DataPreparator():
    def forUpdateWindow(self, data):
        result = pandas.DataFrame(columns=['NAME', 'TIMESTEPS', 'FIRST', 'LAST'])
        names = data['NAME'].unique()
        i = 0
        for name in names:
            i += 1
            is_name = data['NAME'] == name
            data_by_name = data[is_name]
            result.loc[i] = [name, data_by_name.shape[0], data_by_name.iloc[0].TIMESTAMP,
                             data_by_name.iloc[-1].TIMESTAMP]

        return result

    def forTrainWindow(self, market, trends):
        columns = market.columns[3:]
        names = trends['SEARCH_STRING'].unique()
        columns = list(columns)
        names = list(names)
        for name in names:
            columns.append(name)
        return columns, len(columns) - len(names)

    def forPrognosticWindow(self, market, options):
        names = market['NAME'].unique()

        opts = options['Model'] == True
        opts = options[opts]
        opts = opts['Options'].unique()

        return list(names), list(opts)

    def prepareForLSTM(self, data, timesteps):
        prepared_sets = []
        prepared_answers = []
        for j in range(len(data) - timesteps):
            for i in range(j, j + timesteps):
                prepared_sets.append(data[j])
                prepared_answers.append(data[j + 1])

        sets = numpy.array(prepared_sets)
        sets = sets.ravel()
        sets = sets.reshape(len(data) - timesteps, timesteps, 1)

        answers = numpy.array(prepared_answers)
        answers = answers.ravel()
        answers = answers.reshape(len(data) - timesteps, timesteps, 1)

        return sets, answers

    def prepareForDense(self, data, columns):
        categories = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000,
                      5000000, 10000000, 50000000, 100000000, 500000000, 1000000000, 5000000000, 10000000000]

        pre_answers = list(data['DOWNLOADS'])
        answers = []
        sets = []
        data = data[columns]
        data = data.values.tolist()
        i = 0
        for p_a in pre_answers:
            try:
                ans = [0] * len(categories)
                ans[categories.index(p_a)] = 1
                answers.append(ans)
                sets.append(data[i])
            except:
                pass
            i += 1
        return sets, answers

    def prepare_prognose(self, data, app, option, timesteps):
        is_name=data['NAME']==app
        data = data[is_name]
        data = data[option]
        data = list(data)
        return data[len(data)-timesteps:]

    def transform_y_dense(self, y):
        categories = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000,
                      5000000, 10000000, 50000000, 100000000, 500000000, 1000000000, 5000000000, 10000000000]
        res = numpy.where(y == numpy.amax(y))
        return categories[res[0][0]]
