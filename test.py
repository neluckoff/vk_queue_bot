from vk_queue import Users, VkQueue

new_q = VkQueue()


new_q.create_queue()
new_q.add_to_queue(Users(23123, 'sda', 'sda'))
new_q.add_to_queue(Users(458, 'sfa', 'asf'))
new_q.add_to_queue(Users(214, 'sda', 'sda'))
new_q.add_to_queue(Users(9838, 'sda', 'sda'))

print(new_q)

id = new_q.get_first().get_id()
print(id)

new_q.del_person(0)
print(new_q)

id = new_q.get_first().get_id()
print(id)

new_q.del_person(0)
print(new_q)

