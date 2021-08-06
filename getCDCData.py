import requests


class cdcData:
    
    __slots__ = ['cdcCaller','cdcUrl']

    def __init__(self):
        
        self.cdcUrl = 'https://ephtracking.cdc.gov:443/apigateway/api/v1/getCoreHolder/914/2/1/26/20210731,20210730,20210729,20210728,20210727,20210726,20210725,20210724,20210723,20210722,20210721,20210720,20210719,20210718,20210717,20210716,20210715,20210714,20210713,20210712,20210711,20210710,20210709,20210708,20210707,20210706,20210705,20210704,20210703,20210702,20210701/0/0'

    def pullInfo(self):
        response = requests.get(self.cdcUrl)
        d = response.json()
        assert('tableReturnType' in d.keys())
        tableType=d['tableReturnType']
        infoByCounty=d[tableType]
        for item in infoByCounty:
            for key in ['geo','parentGeo','dataValue','reportDay']:
               print(item[key])




if __name__ == '__main__':
    
    obj = cdcData()
    obj.pullInfo()

        
