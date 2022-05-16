class providerReadData:
    def __init__(self, provider, data_type=None, dataframe=None):
        self.provider = provider
        self.data_type = data_type
        self.dataframe = dataframe
    
    def __str__(self):
        if dataframe is not None:
            return self.dataframe
        else: 
            return self.datapush
    
class CsvProvider(providerReadData):
    def __init__(self, provider, data_type=None, dataframe=None):
        super().__init__(provider, data_type=None, dataframe=None)




testclass = CsvProvider('pash', 'csv')
print(testclass.provider)