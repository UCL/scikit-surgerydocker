def main():
    welcome()
    OS_version, py_ver, os_deps = get_values()
    write_docker(OS_version, py_ver, os_deps)

def welcome():
    print('Welcome to the Docker configuration script.')
    print('Answer each questions from the given options or choose NULL \nto get the Dockerfile according to your requirements.')


def get_values():

    cpu_gpu=""
    OS_version=""
    py_ver=""
    os_deps=""
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

    # To install OS level dependencies
    print('Enter an Operating System level dependencies required by the application.')
    print('Seperate each dependency by space e.g. ffmpeg libsm6 :', end=" ")
    os_deps = input().split()




    return OS_version, py_ver, os_deps




def write_docker(OS_version, py_ver, os_deps):
    print(f'''
    FROM {OS_version}
    RUN apt-get update
    RUN apt-get install -y {py_ver} 
    RUN apt-get install -y python3-pip && pip3 install --upgrade pip
    ''')
    for item in os_deps:
        print(f'RUN apt install -y', item)
    








    OS_version=""
    
    
    print()
    OS_version = input()




if __name__=='__main__':
    main()