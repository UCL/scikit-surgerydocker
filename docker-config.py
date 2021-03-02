def main():
    welcome()
    OS_version, py_ver  = get_values()
    write_docker(OS_version, py_ver)

def welcome():
    print('Welcome to the Docker configuration script.')
    print('Answer each questions from the given options or choose NULL \nto get the Dockerfile according to your requirements.')


def get_values():

    cpu_gpu=""
    OS_version=""
    py_ver=""
    cpu_os = ['ubuntu', 'ubuntu:20.04', 'ubuntu:18.04']
    gpu_os = ['nvidia/cuda', 'nvidia/cuda:11.2.1-devel-ubuntu20.04', 'nvidia/cuda:10.2-devel-ubuntu18.04']
    py_version = ['python3.6', 'python3.7', 'python3.8']
    
    # To check if program needs a CPU or GPU
    while(cpu_gpu.lower() not in ['yes', 'no']):
        cpu_gpu=input("Do you need a GPU support? Enter (yes/no): ")
    
    # To provide the options according to the CPU or GPU requirements.
    print('Enter the base operating system for your requirement.')
    print('The available options are:', end=" ")
    if(cpu_gpu.lower == 'n'):
        print(*cpu_os, sep=', ')
        OS_version=input()
    else:
        print(*gpu_os, sep=', ')
        OS_version=input()

    # To install python
    print('Enter the python version for your requirement.')
    print('The available options are:', end=" ")
    print(*py_version, sep=', ')
    py_ver = input()




    return OS_version, py_ver




def write_docker(OS_version, py_ver):
    print(f'''
    FROM {OS_version}
    RUN apt-get update
    RUN apt-get install -y {py_ver}
    
    ''')
    








    OS_version=""
    
    
    print()
    OS_version = input()




if __name__=='__main__':
    main()