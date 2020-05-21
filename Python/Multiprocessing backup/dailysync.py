#!/usr/bin/env python3
from multiprocessing import Pool , cpu_count
import subprocess

src = "/home/student-00-fb7285ba69fe/data/prod/" 
dest = "/home/student-00-fb7285ba69fe/data/prod_backup/" 

p = Pool(cpu_count())
p.apply(subprocess.call, args=(["rsync", "-arq", src, dest],))

