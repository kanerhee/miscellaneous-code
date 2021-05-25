##create dataset within Domo
import logging
from pydomo import Domo
from pydomo.datasets import DataSetRequest, Schema, Column, ColumnType, Policy
from pydomo.datasets import PolicyFilter, FilterOperator, PolicyType, Sorting

# Build an SDK configuration
client_id = '<client_id>'
client_secret = '<client_secret>'
api_host = 'api.domo.com'

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logging.getLogger().addHandler(handler)

domo = Domo(client_id, client_secret, logger_name='account.name', log_level=logging.INFO, api_host=api_host)

datasets = domo.datasets



# Build an SDK configuration
client_id = '<client_id>'
client_secret = '<client_secret>'
api_host = 'api.domo.com'

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logging.getLogger().addHandler(handler)

domo = Domo(client_id, client_secret, logger_name='kane.rhee', log_level=logging.INFO, api_host=api_host)

datasets = domo.datasets

# UPDATE STRINGS TO EXACTLY MATCH DATAFRAME COLUMN NAMES HERE
dsr = DataSetRequest()
dsr.name = 'efaxppi'
dsr.description = ''
dsr.schema = Schema([
                     Column(ColumnType.STRING, 'Brand'),
                     Column(ColumnType.STRING, 'Marketing Region'),
                     Column(ColumnType.STRING, 'Customer Key'),
                     Column(ColumnType.DECIMAL, 'DIDs'),
                     Column(ColumnType.DECIMAL, 'NOP'),
                     Column(ColumnType.DECIMAL, 'Settled Amount'),
                     Column(ColumnType.DECIMAL, 'ARPA')
                        ])



# dataset = datasets.update('ds_id',dsr)

dataset = datasets.create(dsr)
domo.logger.info("Created DataSet " + dataset['id'])
