import api from './index'

export const getUsersApi = () => {
  return api.get('/users/user_list')
}

export const updateUserApi = (telephone:string,data:any)=>{
  return api.put(`/users/user_update?telephone_id=${telephone}`,data)
}

export const createUserApi = (data:any)=>{
  return api.post(`/users/user_create`,data)
}

export const deleteUserApi = (id:number)=>{
  return api.delete(`/users/user_delete?user_id=${id}`)
}