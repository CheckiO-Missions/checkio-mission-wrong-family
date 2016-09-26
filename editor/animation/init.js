//Dont change it
//Dont change it
requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {
        
        var $tryit;

        var io = new extIO({
            animation: function($expl, data){
                if (!data.ext) {
                    return;
                }
                $expl.html(data.ext.explanation);
            },
            functions: {
                js: 'isFamily',
                python: 'is_family'
            }
        });
        io.start();
    }
);
