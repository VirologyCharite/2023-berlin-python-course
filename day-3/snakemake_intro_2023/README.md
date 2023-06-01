## Installation

```
curl -L https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh -o Mambaforge-Linux-x86_64.sh  
bash Mambaforge-Linux-x86_64.sh
```
Follow the instructions, accepting the license (type yes), confirm installation lcoation. 
When you are asked the question

```
Do you wish the installer to initialize Mambaforge
by running conda init?
```

answer with yes. Close and reopen the terminal afterwards. or call 
``` 
source ~/.bashrc
```

Now you have mamba installed and we are ready to install *snakemake*.

``` 
mamba create -c conda-forge -c bioconda -n snakemake snakemake
```

One last call to activate the created snakemake environment and you are ready to go.  

``` 
mamba activate snakemake
```

You can test if everything worked out by checking the version of *snakemake*  

``` 
snakemake --version
``` 



