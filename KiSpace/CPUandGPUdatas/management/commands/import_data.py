from django.core.management.base import BaseCommand
import csv
from CPUandGPUdatas.models import GPU, CPU

class Command(BaseCommand):
    help = 'Import GPU and CPU data from CSV files'

    def add_arguments(self, parser):
        parser.add_argument('gpu_csv_file', type=str, help='Path to the GPU CSV file')
        parser.add_argument('cpu_csv_file', type=str, help='Path to the CPU CSV file')

    def handle(self, *args, **kwargs):
        # Import GPU data
        with open(kwargs['gpu_csv_file'], 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                performance = int(row['Performance'].replace(',', ''))
                GPU.objects.create(name=row['GPU Name'], performance_score=performance)
        self.stdout.write(self.style.SUCCESS(f"GPU data imported from {kwargs['gpu_csv_file']} successfully!"))

        # Import CPU data
        with open(kwargs['cpu_csv_file'], 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                performance = int(row['Performance'].replace(',', ''))
                CPU.objects.create(name=row['CPU Name'], performance_score=performance)
        self.stdout.write(self.style.SUCCESS(f"CPU data imported from {kwargs['cpu_csv_file']} successfully!"))
