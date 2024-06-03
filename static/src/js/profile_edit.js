odoo.define('agd.profile', function (require) {
    "use strict";

    var ajax = require('web.ajax');

    $(document).ready(function () {
        var $ilSelect = $('#il_id');
        var $ilceSelect = $('#ilce_id');
        var $liseSelect = $('#lise_id');

        function loadIlce(il_id, selectedIlceId) {
            if (il_id) {
                ajax.jsonRpc('/get_ilce', 'call', {'il_id': il_id}).then(function (data) {
                    $ilceSelect.empty();
                    $ilceSelect.append($('<option>', {value: '', text: 'İlçe Seçin'}));
                    $.each(data, function (index, ilce) {
                        $ilceSelect.append($('<option>', {value: ilce.id, text: ilce.name, selected: ilce.id == selectedIlceId}));
                    });
                    $ilceSelect.change();
                });
            } else {
                $ilceSelect.empty().append($('<option>', {value: '', text: 'İlçe Seçin'}));
                $liseSelect.empty().append($('<option>', {value: '', text: 'Lise Seçin'}));
            }
        }

        function loadLise(ilce_id, selectedLiseId) {
            if (ilce_id) {
                ajax.jsonRpc('/get_lise', 'call', {'ilce_id': ilce_id}).then(function (data) {
                    $liseSelect.empty();
                    $liseSelect.append($('<option>', {value: '', text: 'Lise Seçin'}));
                    $.each(data, function (index, lise) {
                        $liseSelect.append($('<option>', {value: lise.id, text: lise.name, selected: lise.id == selectedLiseId}));
                    });
                });
            } else {
                $liseSelect.empty().append($('<option>', {value: '', text: 'Lise Seçin'}));
            }
        }

        $ilSelect.change(function () {
            var selectedIlceId = $ilceSelect.data('selected'); // ilce id'sini sakla
            loadIlce($ilSelect.val(), selectedIlceId);
        });

        $ilceSelect.change(function () {
            var selectedLiseId = $liseSelect.data('selected'); // lise id'sini sakla
            loadLise($ilceSelect.val(), selectedLiseId);
        });

        // Initial load for preselected values
        if ($ilSelect.val()) {
            var selectedIlceId = $ilceSelect.data('selected'); // ilce id'sini sakla
            loadIlce($ilSelect.val(), selectedIlceId);
        }
        if ($ilceSelect.val()) {
            var selectedLiseId = $liseSelect.data('selected'); // lise id'sini sakla
            loadLise($ilceSelect.val(), selectedLiseId);
        }
    });
});
