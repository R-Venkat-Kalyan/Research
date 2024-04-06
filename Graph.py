import matplotlib.pyplot as plt

algorithms = ['FIFO', 'DRALBA', 'PSO-GWO', 'RBLMM', 'PMHEFT']
response_time = [0.008, 0.006, 0.005, 0.007, 0.003]
throughput = [800, 900, 1000, 850, 1300]
resource_utilization = [70, 75, 80, 72, 90]

plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.bar(algorithms, response_time, color='skyblue')
plt.title('Response Time Comparison')
plt.xlabel('Algorithms')
plt.ylabel('Response Time (s)')

plt.subplot(1, 3, 2)
plt.bar(algorithms, throughput, color='lightgreen')
plt.title('Throughput Comparison')
plt.xlabel('Algorithms')
plt.ylabel('Throughput')

plt.subplot(1, 3, 3)
plt.bar(algorithms, resource_utilization, color='lightcoral')
plt.title('Resource Utilization Comparison')
plt.xlabel('Algorithms')
plt.ylabel('Resource Utilization (%)')

plt.tight_layout()
plt.show()