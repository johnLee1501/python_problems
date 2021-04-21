import os


def getMinCost(crew_id, job_id):
    crew_id.sort()
    job_id.sort()
    distance = 0
    for n in range(len(crew_id)):
        distance += abs(crew_id[n]-job_id[n])
    return distance

if __name__ == '__main__':
    crew_id_count = int(input().strip())
    crew_id = []
    for _ in range(crew_id_count):
        crew_id_item = int(input().strip())
        crew_id.append(crew_id_item)
    job_id_count = int(input().strip())
    job_id = []
    for _ in range(job_id_count):
        job_id_item = int(input().strip())
        job_id.append(job_id_item)

    result = getMinCost(crew_id, job_id)
    print(result)
