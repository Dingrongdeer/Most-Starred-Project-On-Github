import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
##Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
r = requests.get(url)
print("status code:", r.status_code)

##Store API response in a variable.
response_dict = r.json()

##Process results.
'''
print(response_dict.keys())
'''
print("Total repositiories:", response_dict['total_count'])
##Explore information about the repositories.
repo_dicts = response_dict['items']

'''
print("Repositories returned:", len(repo_dicts))

##Examine the first repository.
repo_dict = repo_dicts[0]

print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)


print("\nSelected information about first repository:")
'''
#names, stars = [],[]
names, plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    #stars.append(repo_dict['stargazers_count'])
    ##Get the project description, if one is available.
    describe =  repo_dict['description']
    if not describe:
        describe = "No description provided."
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label':describe,
        'xlink':repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

'''
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])
'''


##Make visualization.
p_style = LS('#333366', basestyle = LCS)

p_style.title_font_size = 24
p_style.label_font_size = 12
p_style.major_label_font_size = 14

p_config = pygal.Config()
p_config.x_label_rotation = 45
p_config.show_legend = False
p_config.truncate_label = 15
#p_config.show_y_guides = False
p_config.width = 1000


chart = pygal.Bar(p_config, style = p_style )
chart.title = 'Most-Starred JavaScript Project on GitHub'
chart.x_labels = names
chart.y_labels = [x for x in range(0,300000,20000)] 

#chart.add ('', stars)
chart.add ('', plot_dicts)
chart.render_to_file('starred_js.svg')