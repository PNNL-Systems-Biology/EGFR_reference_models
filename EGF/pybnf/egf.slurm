#!/bin/bash
#SBATCH --nodes=4
#SBATCH --time=1000:00:00
#SBATCH --mem=15G
#SBATCH --output=/home/michael/PycharmProjects/EGF/EGF_out.txt

source /home/michael/anaconda3/etc/profile.d/conda.sh
conda activate py36

pybnf -c EGF_ss.conf -t SLURM -o
