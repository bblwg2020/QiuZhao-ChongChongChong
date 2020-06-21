'''
题目描述：
给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。

计算监控树的所有节点所需的最小摄像头数量。

 

示例 1：



输入：[0,0,null,0,0]
输出：1
解释：如图所示，一台摄像头足以监控所有节点。
示例 2：



输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。

提示：

给定树的节点数的范围是 [1, 1000]。
每个节点的值都是 0。

解题思路:

先确定三个状态：
        #状态0 该节点没有被覆盖，但左右子树被覆盖了
        #状态1 该节点及其子节点被覆盖了，但该节点没有摄像头
        #状态2 该节点及其子节点被覆盖了，但该节点有摄像头
再递归更新
最后的结果为状态1和状态2的最小值



'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        #NB 
        #状态0 该节点没有被覆盖，但左右子树被覆盖了
        #状态1 该节点及其子节点被覆盖了，但该节点没有摄像头
        #状态2 该节点及其子节点被覆盖了，但该节点有摄像头
        def getres(root):
            if not root:return(0,0,float('inf'))

            left=getres(root.left)
            right=getres(root.right)
            #状态0 该节点没有被覆盖，但左右子树被覆盖了，👀看左右节点
            dp0=left[1]+right[1]
            #状态1 子节点必须至少有一个为2状态
            dp1=min(left[2]+min(right[1:]),right[2]+min(left[1:]))
            #状态2 易错点：左右需要加起来
            dp2=1+min(left)+min(right)

            return dp0,dp1,dp2
        return min(getres(root)[1:])

