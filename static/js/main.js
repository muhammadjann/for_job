let elWrapper = document.querySelector(".wrapper");

const likeCount = 0;
const disLikeCount = 0;
const getPost = () => {
  fetch("http://127.0.0.1:8000/api/v1/news/")
    .then((res) => res.json())
    .then((data) => {
      data.map((item) => {
        let elInnerWrapper = document.createElement("div");
        elInnerWrapper.innerHTML = `
        <div class='flex justify-between '>
            <div class='w-[32%] h-[350px] relative bg-red-500 rounded-md'>
                <div class='absolute flex items-center -bottom-10 space-x-5'>
                    <button class='bg-black p-2 rounded-md text-white font-semibold'>Like ${likeCount}</button>
                    <button class='bg-black p-2 ml-2 rounded-md text-white font-semibold'>DisLike ${disLikeCount}</button>
                    <button class='bg-black p-2 ml-2 rounded-md text-white font-semibold'>ViewCount</button>
                </div>
            </div>
        <div class='w-[32%] h-[350px] relative bg-blue-500 rounded-md'>
            <div class='absolute flex items-center -bottom-10 space-x-5'>
                <button class='bg-black p-2 rounded-md text-white font-semibold'>Like ${likeCount}</button>
                <button class='bg-black p-2 ml-2 rounded-md text-white font-semibold'>DisLike ${disLikeCount}</button>
                <button class='bg-black p-2 ml-2 rounded-md text-white font-semibold'>ViewCount</button>
            </div>
        </div>
        <div class='w-[32%] h-[350px] relative bg-green-500 rounded-md'>
            <div class='absolute flex items-center -bottom-10 space-x-5'>
                <button class='bg-black p-2 rounded-md text-white font-semibold'>Like ${likeCount}</button>
                <button class='bg-black p-2 ml-2 rounded-md text-white font-semibold'>DisLike ${disLikeCount}</button>
                <button class='bg-black p-2 ml-2 rounded-md text-white font-semibold'>ViewCount</button>
                </div>
            </div>
        </div>
        `;
        elWrapper.appendChild(elInnerWrapper)
      });
    });
};
getPost();
