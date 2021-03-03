def main():
    welcome()
    OS_version, py_ver, os_deps = get_values()
    create_dockerfile(OS_version, py_ver, os_deps)

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
    if(cpu_gpu.lower() == 'no'):
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




def create_dockerfile(OS_version, py_ver, os_deps):

    with open('Dockerfile', 'w+') as f:
        f.write(f'FROM {OS_version}\n')
        f.write('RUN apt-get update\n')
        f.write(f'RUN apt-get install -y {py_ver}\n')
        f.write('RUN apt-get install -y python3-pip && pip3 install --upgrade pip\n')
        for item in os_deps:
            f.write(f'RUN apt install -y {item}\n')
        f.write('COPY src/requirements.txt .\n')
        f.write('RUN pip install -r requirements.txt\n')
        f.write('COPY . .\n')
        f.write('WORKDIR /usr/program/src\n')
        f.write('CMD ["python3", "app.py"]\n')








    OS_version=""
    
    
    print()
    OS_version = input()




if __name__=='__main__':
    main()