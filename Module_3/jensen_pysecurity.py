{
   "user_ID": ObjectID,
   "user_name":String,
   "user_phone" : String,
   
   "Link_User_Role"[{
      "user_ID":ObjectID,
      "roleNo" : ObejctID
         
}]
}

{
   "roleNo" : ObjectID,
   "roleName":String,
   "roleType":String,
   "Link_Role_Permission"[{
       "roleNo" : ObejctID,
       " permissionNo": ObjectID
 
     }]
}

{
   "permissionNo": ObjectID,
   "date"       : String,
   

}
