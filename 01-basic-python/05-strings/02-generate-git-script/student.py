# Write your code here
from textwrap import dedent
def generate_git_script(id):
    tekst = f'''if [ ! -d {id} ]; then
    git clone https://github.com/{id}/project {id}
else
    (cd {id}; git pull)
fi'''
    
    return dedent(tekst)