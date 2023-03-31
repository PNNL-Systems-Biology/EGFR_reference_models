#!/bin/sh

#SBATCH -A hyperbio
#SBATCH -t 168:00:00
#SBATCH -N 1

#SBATCH -n 24
#SBATCH -J egfr_sbt_test
#SBATCH -o egfr_sbt_test.log
#SBATCH -e egfr_sbt_test.err


module purge
module load python/anaconda3.2019.3
source /share/apps/python/anaconda3.2019.3/etc/profile.d/conda.sh
conda init zsh
conda activate te

export PATH=/people/feng626/.conda/envs/te/bin:$PATH

cd /people/feng626/EGFR/EGFRActivation

for i in `seq 0 23`; do
    python ./fitting-test.py $i /people/feng626/EGFR/EGFRActivation/ &
done

wait






