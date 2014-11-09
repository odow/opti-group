#
# Example usage of opti-group
#
# Copyright (C) 2014,  Oscar Dowson
#
import dataio
import model

#
# Presently this is restricted to a SQL Server DB. Modify dataio for others.
# Will make this easier in future.  
#

# Set this flag to true if you have data in a database

#
# There should be two tables in your database.
# One containing the entity data, and the other declaring the variables
# as numeric of categorical.
#
# variable_classification_table(Variable, IsCategorical)
#
#   i.e., if variables 1 & 3 are categorical, and variable 2 is numerical,
#   then the following is required:
#
#   Variable    |   IsCategorical
#   ------------------------------
#   variable1   |       1
#   variable2   |       0
#   variable3   |       1
#
#
# entity_data_table(ID, variable1, variable2, variable3)
#
#   ID  |   v1  |   v2  |   v3
#   ------------------------------
#   A01 |   A   |   1.5 |   Z
#   A02 |   B   |   0.5 |   Y
#   BB1 |   AA  |   3.0 |   Z
#

# ====================================================================================================================
# ====================================================================================================================
f_entity = 'entity_data.txt'                # name of entity_classification_table
f_class = 'classification.txt'              # name of entity_classification_table
data1 = dataio.FlatFile(f_class, f_entity)  # data object
n_groups = 2                                # number of groups to divide into
time_limit = 5                              # time limit for optimisation (seconds)
partition_model = model.PartitionModel(data1, n_groups)
allocation, quality = partition_model.solve(time_limit)


# ====================================================================================================================
# ====================================================================================================================
server = '.'                # location of server. '.' = localhost
database = 'enggen403'      # name of database
entity_tab = 'class_data'   # name of entity_classification_table
class_tab = 'categories'    # name of entity_classification_table
data_a = dataio.DataBase(server, database, entity_tab, class_tab, where='ID > 200')
n_people = 10
data_b = dataio.DataBase(server, database, entity_tab, class_tab, where='ID <= 200')
distribution_model = model.DistributionModel(data_a, data_b, n_people)
allocation1, quality1 = distribution_model.solve(time_limit)
print allocation1
print quality1