#!/bin/bash

date                          #optional, prints out timestamp at the start of the job in stdout file

SPECIES=$1

INPATH="./data/csv/${SPECIES}/"
OUTPATH="./data/gff/${SPECIES}/"

# Check if SPECIES is equal to "B73"
if [ "$SPECIES" = "B73" ]; then
    FORMAL="Zm-B73-REFERENCE-NAM-5.0"
else
    FORMAL="Zm-${SPECIES}-REFERENCE-NAM-1.0"
fi

ZIPPATH_GFF="./ZIP_GFF/${FORMAL}/"
ZIPPATH_CSV="./ZIP_CSV/${FORMAL}/"


mkdir $OUTPATH
mkdir $ZIPPATH_GFF
mkdir $ZIPPATH_CSV

TYPE="APR"
FILENAME_CSV=${TYPE}.csv
FILENAME_GFF=${TYPE}.gff
FORMAL_CSV="${FORMAL}_${TYPE}.csv"
FORMAL_GFF="${FORMAL}_${TYPE}.gff"
echo "Running ${SPECIES} ${TYPE}"

python add_name_to_csv.py $FILENAME_CSV $SPECIES $TYPE $INPATH $OUTPATH $FORMAL_CSV
python add_name_to_gff.py $FILENAME_GFF $SPECIES $TYPE $INPATH $OUTPATH $FORMAL_GFF

mv ${OUTPATH}${FORMAL_GFF} ${ZIPPATH_GFF}
mv ${OUTPATH}${FORMAL_CSV} ${ZIPPATH_CSV}

TYPE="DR"
FILENAME_CSV=${TYPE}.csv
FILENAME_GFF=${TYPE}.gff
FORMAL_CSV="${FORMAL}_${TYPE}.csv"
FORMAL_GFF="${FORMAL}_${TYPE}.gff"
echo "Running ${SPECIES} ${TYPE}"

python add_name_to_csv.py $FILENAME_CSV $SPECIES $TYPE $INPATH $OUTPATH $FORMAL_CSV
python add_name_to_gff.py $FILENAME_GFF $SPECIES $TYPE $INPATH $OUTPATH $FORMAL_GFF

mv ${OUTPATH}${FORMAL_GFF} ${ZIPPATH_GFF}
mv ${OUTPATH}${FORMAL_CSV} ${ZIPPATH_CSV}

TYPE="GQ"
FILENAME_CSV=${TYPE}.csv
FILENAME_GFF=${TYPE}.gff
FORMAL_CSV="${FORMAL}_${TYPE}.csv"
FORMAL_GFF="${FORMAL}_${TYPE}.gff"
echo "Running ${SPECIES} ${TYPE}"

python add_name_to_csv.py $FILENAME_CSV $SPECIES $TYPE $INPATH $OUTPATH $FORMAL_CSV
python add_name_to_gff.py $FILENAME_GFF $SPECIES $TYPE $INPATH $OUTPATH $FORMAL_GFF

mv ${OUTPATH}${FORMAL_GFF} ${ZIPPATH_GFF}
mv ${OUTPATH}${FORMAL_CSV} ${ZIPPATH_CSV}

TYPE="IR"
FILENAME_CSV=${TYPE}.csv
FILENAME_GFF=${TYPE}.gff
FORMAL_CSV="${FORMAL}_${TYPE}.csv"
FORMAL_GFF="${FORMAL}_${TYPE}.gff"
echo "Running ${SPECIES} ${TYPE}"

python add_name_to_csv.py $FILENAME_CSV $SPECIES $TYPE $INPATH $OUTPATH $FORMAL_CSV
python add_name_to_gff.py $FILENAME_GFF $SPECIES $TYPE $INPATH $OUTPATH $FORMAL_GFF

mv ${OUTPATH}${FORMAL_GFF} ${ZIPPATH_GFF}
mv ${OUTPATH}${FORMAL_CSV} ${ZIPPATH_CSV}

TYPE="MR"
FILENAME_CSV=${TYPE}.csv
FILENAME_GFF=${TYPE}.gff
FORMAL_CSV="${FORMAL}_${TYPE}.csv"
FORMAL_GFF="${FORMAL}_${TYPE}.gff"
echo "Running ${SPECIES} ${TYPE}"

python add_name_to_csv.py $FILENAME_CSV $SPECIES $TYPE $INPATH $OUTPATH $FORMAL_CSV
python add_name_to_gff.py $FILENAME_GFF $SPECIES $TYPE $INPATH $OUTPATH $FORMAL_GFF

mv ${OUTPATH}${FORMAL_GFF} ${ZIPPATH_GFF}
mv ${OUTPATH}${FORMAL_CSV} ${ZIPPATH_CSV}

TYPE="STR"
FILENAME_CSV=${TYPE}.csv
FILENAME_GFF=${TYPE}.gff
FORMAL_CSV="${FORMAL}_${TYPE}.csv"
FORMAL_GFF="${FORMAL}_${TYPE}.gff"
echo "Running ${SPECIES} ${TYPE}"

python add_name_to_csv.py $FILENAME_CSV $SPECIES $TYPE $INPATH $OUTPATH $FORMAL_CSV
python add_name_to_gff.py $FILENAME_GFF $SPECIES $TYPE $INPATH $OUTPATH $FORMAL_GFF

mv ${OUTPATH}${FORMAL_GFF} ${ZIPPATH_GFF}
mv ${OUTPATH}${FORMAL_CSV} ${ZIPPATH_CSV}

TYPE="Z"
FILENAME_CSV=${TYPE}.csv
FILENAME_GFF=${TYPE}.gff
FORMAL_CSV="${FORMAL}_${TYPE}.csv"
FORMAL_GFF="${FORMAL}_${TYPE}.gff"
echo "Running ${SPECIES} ${TYPE}"

python add_name_to_csv.py $FILENAME_CSV $SPECIES $TYPE $INPATH $OUTPATH $FORMAL_CSV
python add_name_to_gff.py $FILENAME_GFF $SPECIES $TYPE $INPATH $OUTPATH $FORMAL_GFF

mv ${OUTPATH}${FORMAL_GFF} ${ZIPPATH_GFF}
mv ${OUTPATH}${FORMAL_CSV} ${ZIPPATH_CSV}

cd ./ZIP_GFF/
tar -czf ${FORMAL}_nonB_GFF.tar.gz ${FORMAL}
cd ..
cd ./ZIP_CSV/
tar -czf ${FORMAL}_nonB_CSV.tar.gz ${FORMAL}

date                          #optional, prints out timestamp when the job ends
#End of file
