import { useEffect } from 'react';

const BlogList = ({ blogs1, handleDelete }) => {

    useEffect(() => {
        console.log('hi from the List');
    })

    return (
        <div className="blog-list">
            {blogs1.map(blog => (
                <div className="blog_preview" key={blog.id}>
                    <h2>{ blog.title }</h2>
                    <p>{ blog.author }</p>
                    <button onClick={() => handleDelete(blog.id)}>delete</button>
                </div>
            ))}
        </div>
    );
}
 
export default BlogList;