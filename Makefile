.PHONY : env
env :
	mamba env create -f environment.yml -p ~/envs/ligo
	bash -ic 'conda activate ligo;python -m ipykernel install --user --name ligo --display-name "IPython - LIGO"'

.PHONY : html
html : 
	jupyter-book build .
	
.PHONY : html-hub
html-hub :
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	bash -ic 'cd _build/html; echo "https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html"; python -m http.server'

.PHONY : clean
clean :
	rm -f figures/*.png
	rm -f GW150914_data.csv
	rm -f audio/*.wav
	rm -rf _build