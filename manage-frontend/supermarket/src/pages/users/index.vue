<script setup lang="ts">
import { getUsersApi, updateUserApi, createUserApi, deleteUserApi } from '@/api/user.ts'
import { onMounted } from 'vue';
import { Plus } from '@element-plus/icons-vue'
import { ref } from 'vue'
import { ElMessage } from 'element-plus'

const tableData = ref([])
const dialogVisible = ref(false)
const operaName = ref('新增')
const telephoneValue = ref('')
const formValue = ref({
    name: '',
    telephone: '',
    role: '',
    address: '',
    description: ''
})

onMounted(() => {
    getUserList()
})

const getUserList = () => {
    getUsersApi().then((res: any) => {
        console.log('res:', res)
        tableData.value = res.data
    })
}

const modifyUser = (row: any) => {
    dialogVisible.value = true
    operaName.value = '修改用户'
    formValue.value = {
        name: row.name,
        telephone: row.telephone,
        role: row.role,
        address: row.address,
        description: row.description
    }
    telephoneValue.value = row.telephone
}

const deleteUser = (id: number) => {
    deleteUserApi(id).then(() => {
        ElMessage({
            message: '删除成功',
            type: 'success'
        })

        getUserList();
    })
}

const addUser = () => {
    dialogVisible.value = true
    operaName.value = '新增用户'
}

const userInfo = () => {
    if (operaName.value === '新增用户') {
        createUserApi(formValue.value).then((res: any) => {
            if (res.code === 200) {
                ElMessage({
                    message: '操作成功',
                    type: 'success'
                })
                getUserList();
                formValue.value = {
                    name: '',
                    telephone: '',
                    role: '',
                    address: '',
                    description: ''
                }
            } else {
                ElMessage({
                    message: '操作成功',
                    type: 'error'
                })
            }
        }).finally(() => {
            dialogVisible.value = false;
        })
    } else if (operaName.value === '修改用户') {
        console.log('telephoneValue:', telephoneValue.value)
        updateUserApi(telephoneValue.value, formValue.value).then((res: any) => {
            if (res.code === 200) {
                ElMessage({
                    message: '操作成功',
                    type: 'success'
                })
                getUserList();
                formValue.value = {
                    name: '',
                    telephone: '',
                    role: '',
                    address: '',
                    description: ''
                }
            } else {
                ElMessage({
                    message: '操作成功',
                    type: 'error'
                })
            }
        }).finally(() => {
            dialogVisible.value = false;
        })
    }

}
</script>

<template>
    <div class="container">
        <div class="header">
            <el-button :icon="Plus" type="primary" @click="addUser">新增</el-button>
        </div>
        <div class="context">
            <el-table :data="tableData">
                <el-table-column label="ID" prop="id" width="60px"></el-table-column>
                <el-table-column label="姓名" prop="name" width="100px"></el-table-column>
                <el-table-column label="手机号" prop="telephone" min-width="120px"></el-table-column>
                <el-table-column label="角色" prop="role" width="100px"></el-table-column>
                <el-table-column label="地址" prop="address" min-width="120px"></el-table-column>
                <el-table-column label="创建时间" prop="create_time" width="170px"></el-table-column>
                <el-table-column label="更新时间" prop="update_time" width="170px"></el-table-column>
                <el-table-column label="描述" prop="description" min-width="150px"></el-table-column>
                <el-table-column label="操作" fixed="right">
                    <template #default="{ row }" direction="horizontal" size="small">
                        <el-space>
                            <el-button size="small" type="primary" @click="modifyUser(row)">修改</el-button>
                            <el-button size="small" type="danger" @click="deleteUser(row.id)">删除</el-button>
                        </el-space>

                    </template>
                </el-table-column>
            </el-table>
        </div>
    </div>

    <el-dialog v-model="dialogVisible" :title="operaName" width="500">
        <div class="dialogStyle">
            <el-form :model="formValue" label-suffix=":">
                <el-form-item label="姓名">
                    <el-input v-model="formValue.name" style="width: 350px;" />
                </el-form-item>
                <el-form-item label="电话">
                    <el-input v-model="formValue.telephone" style="width: 350px;" />
                </el-form-item>
                <el-form-item label="角色">
                    <el-select v-model="formValue.role" style="width: 350px;"
                        :options="[{ label: '管理员', value: 'admin' }, { label: '普通用户', value: 'user' }]">
                    </el-select>
                </el-form-item>
                <el-form-item label="地址">
                    <el-input v-model="formValue.address" style="width: 350px;" />
                </el-form-item>
                <el-form-item label="描述">
                    <el-input v-model="formValue.description" style="width: 350px;" />
                </el-form-item>
            </el-form>
        </div>

        <div class="footer">
            <el-space>
                <el-button @click="() => dialogVisible = false">取消</el-button>
                <el-button type="primary" @click="userInfo">确定</el-button>
            </el-space>
        </div>

    </el-dialog>
</template>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    gap: 10px;
    height: 100%;
}

.header {
    width: 100%;
    padding: 6px;
    background-color: #fff;
    box-sizing: border-box;
}

.context {
    flex: 1;
    background-color: #fff;
}

.dialogStyle {
    display: flex;
    justify-content: center;
    align-items: center;
}

.footer {
    display: flex;
    justify-content: flex-end;
}
</style>