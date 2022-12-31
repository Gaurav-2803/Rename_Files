import os

season_list = ['S00', 'S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S07', 'S08', 'S09', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35', 'S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45', 'S46', 'S47', 'S48', 'S49',
               'S50', 'S51', 'S52', 'S53', 'S54', 'S55', 'S56', 'S57', 'S58', 'S59', 'S60', 'S61', 'S62', 'S63', 'S64', 'S65', 'S66', 'S67', 'S68', 'S69', 'S70', 'S71', 'S72', 'S73', 'S74', 'S75', 'S76', 'S77', 'S78', 'S79', 'S80', 'S81', 'S82', 'S83', 'S84', 'S85', 'S86', 'S87', 'S88', 'S89', 'S90', 'S91', 'S92', 'S93', 'S94', 'S95', 'S96', 'S97', 'S98', 'S99', 'S100']

episode_list = ['E01', 'E02', 'E03', 'E04', 'E05', 'E06', 'E07', 'E08', 'E09', 'E10', 'E11', 'E12', 'E13', 'E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20', 'E21', 'E22', 'E23', 'E24', 'E25', 'E26', 'E27', 'E28', 'E29', 'E30', 'E31', 'E32', 'E33', 'E34', 'E35', 'E36', 'E37', 'E38',
                'E39', 'E40', 'E41', 'E42', 'E43', 'E44', 'E45', 'E46', 'E47', 'E48', 'E49', 'E50', 'E51', 'E52', 'E53', 'E54', 'E55', 'E56', 'E57', 'E58', 'E59', 'E60', 'E61', 'E62', 'E63', 'E64', 'E65', 'E66', 'E67', 'E68', 'E69', 'E70', 'E71', 'E72', 'E73', 'E74', 'E75', 'E76', 'E77', 'E78', 'E79', 'E80', 'E81', 'E82', 'E83', 'E84', 'E85', 'E86', 'E87', 'E88', 'E89',
                'E90', 'E91', 'E92', 'E93', 'E94', 'E95', 'E96', 'E97', 'E98', 'E99', 'E100', 'E101', 'E102', 'E103', 'E104', 'E105', 'E106', 'E107', 'E108', 'E109', 'E110', 'E111', 'E112', 'E113', 'E114', 'E115', 'E116', 'E117',
                'E118', 'E119', 'E120', 'E121', 'E122', 'E123', 'E124', 'E125', 'E126', 'E127', 'E128', 'E129', 'E130', 'E131', 'E132', 'E133', 'E134', 'E135', 'E136', 'E137', 'E138', 'E139', 'E140', 'E141', 'E142', 'E143', 'E144', 'E145', 'E146', 'E147', 'E148', 'E149', 'E150', 'E151', 'E152', 'E153', 'E154', 'E155', 'E156', 'E157', 'E158', 'E159', 'E160', 'E161', 'E162', 'E163', 'E164', 'E165', 'E166', 'E167', 'E168',
                'E169', 'E170', 'E171', 'E172', 'E173', 'E174', 'E175', 'E176', 'E177', 'E178', 'E179', 'E180', 'E181', 'E182', 'E183', 'E184', 'E185',
                'E186', 'E187', 'E188', 'E189', 'E190', 'E191', 'E192', 'E193', 'E194', 'E195', 'E196', 'E197', 'E198', 'E199', 'E200']


def check_sea_ep(file, array):
    for i in range(len(array)):
        if array[i] in file:
            return array[i]


def chk_ext(file):
    extenstion = ""
    for i in range(len(file)-1, -1, -1):
        if file[i] != ".":
            extenstion += file[i]
        else:
            break
    extenstion += "."
    return extenstion[::-1]


def file_const(files_list, series_name):
    for i in range(len(files_list)):
        old_file_name = files_list[i]
        season = check_sea_ep(old_file_name, season_list)
        episode = check_sea_ep(old_file_name, episode_list)
        if season and episode:
            extenstion = chk_ext(old_file_name)
            new_file_name = f'{series_name} {season}{episode} {extenstion}'
            os.system(f'ren "{old_file_name}" "{new_file_name}"')
            print(
                f"\n============================================\nName Changed from -> {old_file_name} to -> {new_file_name}\n============================================")


path = input("Folder Path : ")
series_name = input("New File Name : ")

os.chdir(path)
path = os.getcwd()
print(
    f"============================================\nPath Changed to -> {path}\n============================================")
files_list = os.listdir()
# print(files_list)
file_const(files_list, series_name)

# for i in range(1, len(files_list)):
#     sub_path = files_list[i]
#     os.chdir(sub_path)
#     sub_path = os.getcwd()
#     print(
#         f"============================================\nPath Changed to -> {sub_path}\n============================================")
#     files_list1 = os.listdir()
#     print(files_list1)
#     file_const(files_list1, series_name)
#     os.chdir(path)
#     path = os.getcwd()
#     print(
#         f"============================================\nPath Changed to -> {path}\n============================================")

# Generate List
""" li = []
for i in range(0, 10):
    # if i < 10:
    #     st = f"S0{i}"
    # else:
    st = f"S{i}"
    li.append(st)
print(li)
 """
