document.addEventListener('DOMContentLoaded', () => {

  if(document.querySelectorAll('.ban-lock')){
    document.querySelectorAll('.ban-lock').forEach(item => {
      item.onmouseover = () =>{
        item.classList.remove('fa-lock');
        item.classList.add('fa-unlock-alt');
      }
      item.onmouseout = () =>{
        item.classList.remove('fa-unlock-alt');
        item.classList.add('fa-lock');
      }
    });

  }


  if(document.querySelector('#profile_form')){
  document.querySelector('#profile_form').style.display = 'none';
  document.querySelector('#updatebutton').onclick = () => {
    document.querySelector('#profile_form').style.display = 'block';
    document.querySelector('#updatebutton').style.display = 'none';
    document.querySelector('.alert').style.display = 'none';
  };
  document.querySelector('#closeform').onclick = () => {
    document.querySelector('#profile_form').style.display = 'none';
    document.querySelector('#updatebutton').style.display = 'block';
  };
}


if(document.querySelectorAll('.indexpage_activity')){
  console.log("We have it");
  document.querySelectorAll('.indexpage_activity').forEach(item => {
    item.onclick = () =>{
      console.log("Here I am!");
      window.location.href = `http://127.0.0.1:8000/activities/${item.dataset.id}`;
    }
  });

}


if(document.querySelector('#delete_activity_page')){
  document.querySelector('#delete_activity_page').style.display = 'none';
}
if(document.querySelector('.fontawesome_common')){
  console.log("Font awesome common is here");
  document.querySelectorAll('.fontawesome_common').forEach(item => {
    item.onmouseover = () =>{
      item.classList.remove('far');
      item.classList.add('fas');
    }
  });
  document.querySelectorAll('.fontawesome_common').forEach(item => {
    item.onmouseout = () =>{
      item.classList.remove('fas');
      item.classList.add('far');
    }
  });
  document.querySelector('#delete_activity_page').style.display = 'none';
  if(document.querySelector('.fontawesome_delete_permanent')){
    console.log("Permanent delete!");
    document.querySelectorAll('.fontawesome_delete_permanent').forEach(item => {
      item.onclick = (event) =>{
        const element = item.parentElement.parentElement.children[2];
        document.querySelector('#delete_activity_page').style.display = 'block';
        const q = document.querySelector('#delete_activity_page_content_js');
        const p = document.createElement('div');
        p.classList.add('delete_activity_page_content_js1')
        p.innerHTML = `

        <p>Are you sure you want to delete your Activity?</p>
        <p>${element.innerHTML}</p>

        `;
        q.appendChild(p);
        document.querySelector('.delete_activity_page_content_js_buttons_1').innerHTML = `

        <a href="http://127.0.0.1:8000/permanent-delete/${item.dataset.id}" class="btn btn-outline-primary common_button">Confirm</a>


        `;
        event.stopPropagation();
      }
    });
  }



  if(document.querySelector('.fontawesome_delete_comment')){
    console.log("Delete Comment");
    document.querySelectorAll('.fontawesome_delete_comment').forEach(item => {
      item.onclick = (event) =>{
        const element = item.parentElement.parentElement.children[2];
        document.querySelector('#delete_activity_page').style.display = 'block';
        const q = document.querySelector('#delete_activity_page_content_js');
        const p = document.createElement('div');
        p.classList.add('delete_activity_page_content_js1')
        p.innerHTML = `

        <p>Are you sure you want to delete the Comment?</p>
        <p>${element.innerHTML}</p>

        `;
        q.appendChild(p);
        document.querySelector('.delete_activity_page_content_js_buttons_1').innerHTML = `

        <a href="http://127.0.0.1:8000/comment-delete/${item.dataset.id}" class="btn btn-outline-primary common_button">Confirm</a>


        `;
        event.stopPropagation();
      }
    });
  }




  document.querySelectorAll('.fontawesome_delete').forEach(item => {
    item.onclick = (event) => {
      const element = item.parentElement.parentElement.children[2];
      document.querySelector('#delete_activity_page').style.display = 'block';
      const q = document.querySelector('#delete_activity_page_content_js');
      const p = document.createElement('div');
      p.classList.add('delete_activity_page_content_js1')
      p.innerHTML = `

      <p>Are you sure you want to remove your Activity?</p>
      <p>${element.innerHTML}</p>

      `;
      q.appendChild(p);
      document.querySelector('.delete_activity_page_content_js_buttons_1').innerHTML = `

      <a href="http://127.0.0.1:8000/index/delete-activity/${item.dataset.id}" class="btn btn-outline-primary common_button">Confirm</a>

      `;

      event.stopPropagation();
    }
  });
  document.querySelectorAll('.fontawesome_edit').forEach(item => {
    item.onclick = (event) => {
      event.stopPropagation();
    }
  });


  document.querySelector('#closeform').onclick = () => {
    document.querySelector('.delete_activity_page_content_js1').remove();
    document.querySelector('#delete_activity_page').style.display = 'none';
  }

  document.querySelector('.cancel_delete').onclick = () => {
    document.querySelector('.delete_activity_page_content_js1').remove();
    document.querySelector('#delete_activity_page').style.display = 'none';
  }

}

});
