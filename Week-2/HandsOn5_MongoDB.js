// =====================================
// HANDSON 5 : MONGODB
// =====================================

// INSERT

db.feedback.insertOne({
    student_id:101,
    course_id:201,
    rating:5,
    comment:"Excellent Course"
});

// FIND

db.feedback.find();

// UPDATE

db.feedback.updateOne(
    {student_id:101},
    {$set:{rating:4}}
);

// DELETE

db.feedback.deleteOne(
    {student_id:101}
);

// AGGREGATION

db.feedback.aggregate([
{
    $group:{
        _id:"$course_id",
        avgRating:{$avg:"$rating"}
    }
}
]);

// INDEX

db.feedback.createIndex(
    {student_id:1}
);