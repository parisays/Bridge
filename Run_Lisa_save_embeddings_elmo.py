#PBS -S /bin/bash

#PBS -qgpu
#PBS -lnodes=1
#PBS -lwalltime=10:00:00

module load eb
module load Python/3.6.3-foss-2017b
module load CUDA/9.0.176
module load cuDNN/7.0.5-CUDA-9.0.176
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:/hpc/eb/Debian9/cuDNN/7.0.5-CUDA-9.0.176/lib64:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH:/home/samigpu/Codes/GoogleLM1b/
cd ~/Codes/Bridge

text_encoder='elmo' #universal_large elmo glove tf_token
past_window=0

embedding_type='word_emb'
python encode_stimuli_in_context.py --root /home/samigpu/Codes/ --text_encoder=$text_encoder --embedding_type=$embedding_type --past_window=$past_window --context_mode=sentence

embedding_type='lstm_outputs1'
python encode_stimuli_in_context.py --root /home/samigpu/Codes/ --text_encoder=$text_encoder --embedding_type=$embedding_type --past_window=$past_window --context_mode=sentence

embedding_type='lstm_outputs2'
python encode_stimuli_in_context.py --root /home/samigpu/Codes/ --text_encoder=$text_encoder --embedding_type=$embedding_type --past_window=$past_window --context_mode=sentence

embedding_type='elmo'
python encode_stimuli_in_context.py --root /home/samigpu/Codes/ --text_encoder=$text_encoder --embedding_type=$embedding_type --past_window=$past_window --context_mode=sentence