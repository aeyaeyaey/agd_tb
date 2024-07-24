odoo.define('agd.profile', function (require) {
    "use strict";

    var ajax = require('web.ajax');

    $(document).ready(function () {
        var $ilSelect = $('#il_id');
        var $uniSelect = $('#uni_id');
        var $ilceSelect = $('#ilce_id');
        var $fakSelect = $('#fak_id');
        var $liseSelect = $('#lise_id');
        var $bolumSelect = $('#bolum_id');

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

        function loadfak(uni_id, selectedfakId) {
            if (uni_id) {
                ajax.jsonRpc('/get_fak', 'call', {'uni_id': uni_id}).then(function (data) {
                    $fakSelect.empty();
                    $fakSelect.append($('<option>', {value: '', text: 'Fakülte Seçin'}));
                    $.each(data, function (index, fak) {
                        $fakSelect.append($('<option>', {value: fak.id, text: fak.name, selected: fak.id == selectedfakId}));
                    });
                    $fakSelect.change();
                });
            } else {
                $fakSelect.empty().append($('<option>', {value: '', text: 'Fakülte Seçin'}));
                $bolumSelect.empty().append($('<option>', {value: '', text: 'Bolum Seçin'}));
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

        function loadbolum(fak_id, selectedbolumId) {
            if (fak_id) {
                ajax.jsonRpc('/get_bolum', 'call', {'fak_id': fak_id}).then(function (data) {
                    $bolumSelect.empty();
                    $bolumSelect.append($('<option>', {value: '', text: 'Bölüm Seçin'}));
                    $.each(data, function (index, bolum) {
                        $bolumSelect.append($('<option>', {value: bolum.id, text: bolum.name, selected: bolum.id == selectedbolumId}));
                    });
                });
            } else {
                $bolumSelect.empty().append($('<option>', {value: '', text: 'Bölüm Seçin'}));
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

        $uniSelect.change(function () {
            var selectedfakId = $fakSelect.data('selected'); // fak id'sini sakla
            loadfak($uniSelect.val(), selectedfakId);
        });

        $fakSelect.change(function () {
            var selectedbolumId = $bolumSelect.data('selected'); // bölüm id'sini sakla
            loadbolum($fakSelect.val(), selectedbolumId);
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
        if ($uniSelect.val()) {
            var selectedfakId = $fakSelect.data('selected'); // fak id'sini sakla
            loadfak($uniSelect.val(), selectedfakId);
        }
        if ($fakSelect.val()) {
            var selectedbolumId = $bolumSelect.data('selected'); // lise id'sini sakla
            loadbolum($fakSelect.val(), selectedbolumId);
        }
    });
});
