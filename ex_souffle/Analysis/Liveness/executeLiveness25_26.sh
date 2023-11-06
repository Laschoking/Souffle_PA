# !bash.sh
doop=/home/kotname/Documents/Diplom/Code/doop/master

echo $doop

mkdir prof25_26

rm ../../out/Liveness/25/*.csv
rm ../../out/Liveness/26/*.csv

souffle Liveness.dl -F $doop/out/25/database -D ../../out/Liveness/25 -j4 -pLiveness25
souffle Liveness.dl -F $doop/out/26/database -D ../../out/Liveness/26 -j4 -pLiveness26


cd ../../out/Liveness

rm vgl25_26/*

cp 25/Def.csv vgl25_26/Def1.csv
cp 25/Use.csv vgl25_26/Use1.csv
cp 25/InterproceduralDefUse.csv vgl25_26/InterproceduralDefUse1.csv

cp 26/Def.csv vgl25_26/Def2.csv
cp 26/Use.csv vgl25_26/Use2.csv
cp 26/InterproceduralDefUse.csv vgl25_26/InterproceduralDefUse2.csv


cd ../../Analysis/Liveness

souffle CompareLiveness.dl -F ../../out/Liveness/vgl25_26 -D ../../out/Liveness/vgl25_26 -j4 -pCompLiveness25_26

mv Liveness25 prof25_26/
mv Liveness26 prof25_26/
mv CompLiveness25_26 prof25_26/
cd prof25_26/
souffleprof -j Liveness25 
souffleprof -j Liveness26
souffleprof -j CompLiveness25_26 

mv 1.html Liveness25.html
mv 2.html Liveness26.html
mv 3.html CompLiveness25_26.html
