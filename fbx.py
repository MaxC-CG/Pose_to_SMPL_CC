from pyfbx import *

# 创建FBX管理器和场景
manager = Manager()
scene = Scene(manager)

# 加载FBX文件
filename = './fbx/Jumping.fbx'  # 替换为您的FBX文件路径
FbxCommon.LoadScene(manager.sdk_manager, scene._me, filename)

# 打印场景中的根节点名称
root_node = scene.root_node
print("Root node name:", root_node.name)

# 遍历场景中的所有节点并打印它们的名称
for node in scene.scene_nodes:
    print("Node name:", node.name)
