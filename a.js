const cameraDatas = [
    {
        _id: '1',
        name: '101入口',
        room_id: 101,
    }
]

//それぞれの判定のプロパティをカメラレコードに追加
cameraData.forEach((cameraData) => {
    cameraData.人 = false;
    cameraData.光 = false;
    cameraData.鍵 = false;
});

const 人の判定 = 人がいるか判定('101入口のカメラ画像のデータ');

//人がいるか？
if (人の判定) {
    cameraData[0].人 = true;
}