<?php 
/**
 * Countries list using ISO 3166-1 alpha-2
 *
 * Author: Eduardo Estevez <estevez121@gmail.com>
 * Last Updated: 03/01/2016
 * @version
 * @package
 * @subpackage
 * @copyright
 * @license
 *
 * The data file iso_3166-1_alpha-2.json has been taken from the project https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes
 *
 *
 */

/**
 * country_code_iso
 *
 *
 */
function country_code_iso() {

    
    $file = 'iso_3166-1_alpha-2.json';
    $json = json_decode( file_get_contents($file) , true);
    
    if ( !is_null( $json ) ){
        
        print ( '<select id="inf_custom_Country1" class="form-control" name="inf_custom_Country1">'.PHP_EOL );
        print ( '<option value="">Select</option>'.PHP_EOL );

        foreach ($json as $attr) {

             $name =  $attr['name'];
             $alpha_2 = $attr['alpha-2'];
            
             #print ( $name.' '.$alpha_2.PHP_EOL );
             print ( '<option value="'.$alpha_2.'">'.$name.'</option>'.PHP_EOL );
          
        }
        
        print ( '</select>'.PHP_EOL );

    }


}

country_code_iso();

?>