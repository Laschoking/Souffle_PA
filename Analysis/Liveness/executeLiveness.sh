# !bash.sh
doop=/home/kotname/Documents/Diplom/Code/doop/master

echo $doop
: '
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

'
rm ../../out/Liveness/7/*.csv
rm ../../out/Liveness/8/*.csv

souffle Liveness.dl -F $doop/out/7PDG_Example_reordered/database -D ../../out/Liveness/7

souffle Liveness.dl -F $doop/out/8PDG_Example_re_addSm/database -D ../../out/Liveness/8


cd ../../out/Liveness

rm vgl7_8/*

cp 7/Def.csv vgl7_8/Def1.csv
cp 7/Use.csv vgl7_8/Use1.csv
cp 7/InterproceduralDefUse.csv vgl7_8/InterproceduralDefUse1.csv

cp 8/Def.csv vgl7_8/Def2.csv
cp 8/Use.csv vgl7_8/Use2.csv
cp 8/InterproceduralDefUse.csv vgl7_8/InterproceduralDefUse2.csv


cd ../../Analysis/Liveness

souffle CompareLiveness.dl -F ../../out/Liveness/vgl7_8 -D ../../out/Liveness/vgl7_8

