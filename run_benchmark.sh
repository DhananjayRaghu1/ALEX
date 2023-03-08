#!/usr/bin/env bash

function do_benchmark()
{
    echo ""
    ./build/benchmark --keys_file=$1 --keys_file_type=binary --init_num_keys=10000000 --total_num_keys=20000000 --batch_size=1000000 --insert_frac=0.5 --lookup_distribution=zipf --print_batch_stats --dataset_name=$2
    echo ""
}

if [ "$#" -eq  "2" ]; then

    # run the benchmark
    do_benchmark $1 $2

    # generate graphs
    python3 generate_graphics.py $2
    
else
    echo ""
    echo "  No arguments supplied !"
    echo ""
    echo "      ./run_benchmark.sh path_to_dataset_file dataset_name"
    echo ""
    echo "      eg : ./run_benchmark.sh resources/longitudes-200M.bin.data longitudes"
    echo ""
fi

