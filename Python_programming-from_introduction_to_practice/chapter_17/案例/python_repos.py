import requests

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")  #查看响应是否成功
#将API响应赋给一个变量
reponse_dict = r.json()
print(f"Total repositories: {reponse_dict['total_count']}")

#探索有关仓库的信息
repo_dicts = reponse_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

#研究第一个仓库
repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)
print(f"\nSelected information about first repository: ")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")