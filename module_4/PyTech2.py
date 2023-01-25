Student Schema :

student_id:{

type:Number

},

first_name:{

type:String

},

last_name:{

type:String

},

//one student can have many enrollments

//so array of enrollmentID will come here

enrollments:[{

type:ObjectId,

ref:"Enrollment"

}],

//one student enrolls in many courses

//so we will keep all courseId in which student is enrolled

courses:[

{

type:ObjectId,

ref:"Course"

}

]

Enrollment Schema :

term :{

type:String,

},

gpa:{

type:Number,

default:8.0

},

start_date:{

type:Date

},

end_date:{

type:Date

},

//one enrollment can have multiple courses

courses:[

{

type:ObjectId,

ref:"Course"

}

]

Course Schema

course_id:{

type:ObjectId

},

description:{

type:String

},

instructor:{

firstName:{

type:String

},

lastName:{

type:String

}

},

grade:{

type:String

}
