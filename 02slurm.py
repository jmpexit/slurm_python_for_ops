from math import ceil

if __name__ == "__main__":
    print("Привет, Слёрм!")

containers_number = 68796
pod_capacity = 4 # containers
node_capacity = 117 # pods
node_number_per_center = 21 #nods
pod_number = ceil(containers_number / pod_capacity)
node_number = ceil(pod_number / node_capacity)
center_number = ceil(node_number / node_number_per_center)

print("datacenters number - ", center_number)

ram_per_node = 16*1024
ram_per_container = 30
total_ram = (node_number * ram_per_node)
containers_ram = containers_number * ram_per_container
unused_ram = total_ram - containers_ram

print(unused_ram)

unused_ram_gb = unused_ram // 1024

print(unused_ram_gb)

unused_ram_mb = unused_ram % 1024

print(unused_ram_mb)
