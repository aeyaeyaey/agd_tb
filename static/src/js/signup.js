odoo.define('agd.signup', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var csrf_token = core.csrf_token;

    $(document).ready(function () {
        $('#il_id').change(function () {
            var il_id = parseInt($(this).val(), 10);
            console.log("Selected il_id:", il_id);

            ajax.jsonRpc('/get_districts', 'call', {'il_id': il_id, 'csrf_token': csrf_token}).then(function (data) {
                console.log("Districts Data:", data);
                if (data.error) {
                    console.error("Hata:", data.error);
                    return;
                }
                var $ilce = $('#ilce_id');
                $ilce.empty().append('<option value="">İlçe Seçin</option>');
                $.each(data, function (index, ilce) {
                    $ilce.append('<option value="' + ilce.id + '">' + ilce.name + '</option>');
                });
            }).catch(function (error) {
                console.error("İlçeleri yüklerken hata oluştu:", error);
            });
        });

        $('#ilce_id').change(function () {
            var ilce_id = parseInt($(this).val(), 10);
            console.log("Selected ilce_id:", ilce_id);

            ajax.jsonRpc('/get_schools', 'call', {'ilce_id': ilce_id, 'csrf_token': csrf_token}).then(function (data) {
                console.log("Schools Data:", data);
                if (data.error) {
                    console.error("Hata:", data.error);
                    return;
                }
                var $lise = $('#lise_id');
                $lise.empty().append('<option value="">Lise Seçin</option>');
                $.each(data, function (index, lise) {
                    $lise.append('<option value="' + lise.id + '">' + lise.name + '</option>');
                });
            }).catch(function (error) {
                console.error("Liseleri yüklerken hata oluştu:", error);
            });
        });
    });
});
