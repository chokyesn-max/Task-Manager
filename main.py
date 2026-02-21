from manager import TaskManager

m = TaskManager()

while True:
    print("\n=== TASK MANAGER ===")
    print("1. Tambah Task")
    print("2. Lihat task")
    print("3. Tandai selesai")
    print("4. Hapus task selesai")
    print("5. Keluar")
    

    pilih = input("Pilih: ")

    if pilih == "1":
        title = input("Judul: ")
        m.add_task(title)
        print("Task Added")
    elif pilih == "2":
        tasks = m.get_tasks()

        for t in tasks:
            status = "[X]" if t.done else "[ ]"
            print (t.id, status, t.title)
    elif pilih == "3":
        task_id = int(input("Masukan ID Task: "))
        m.mark_done_by_id(task_id)
        print("task ditandai selesai")
    elif pilih == "4":
        m.delete_done()
        print("Task dihapus")
    elif pilih == "5":
        break
    else:
        print("Input tidak valid")